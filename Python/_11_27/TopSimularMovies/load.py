import pandas as pd
import pickle
from pymongo import MongoClient


def load_dict_of_table():
    d_films, d_actors, d_tags = {}, {}, {}
    films = pd.read_table('table_data/MovieCodes_IMDB.tsv', low_memory=False)
    films = films[films['language'].isin(('en', 'ru'))]
    for x in films.itertuples():
        temp_fid = int(x[1][2:])
        d_films[temp_fid] = d_films.get(temp_fid, {'name': set(),
                                                   'rate': 0,
                                                   'director': '',
                                                   'actors': set(),
                                                   'tags': set()})
        d_films[temp_fid]['name'].add(x[3])
    del films

    for x in pd.read_table('table_data/Ratings_IMDB.tsv').itertuples():
        temp_fid = int(x[1][2:])
        if d_films.get(temp_fid):
            d_films[temp_fid]['rate'] = x[2]

    for x in pd.read_table('table_data/ActorsDirectorsCodes_IMDB.tsv').itertuples():
        temp_fid = int(x[1][2:])
        if d_films.get(temp_fid):
            temp_aid = int(x[3][2:])
            d_actors[temp_aid] = d_actors.get(temp_aid, {'name': '', 'films': set()})
            d_actors[temp_aid]['films'].add(temp_fid)
            if x[4] == 'actor':
                d_films[temp_fid]['actors'].add(int(x[3][2:]))
            elif x[4] == 'director':
                d_films[temp_fid]['director'] = int(x[3][2:])
    for x in pd.read_table('table_data/ActorsDirectorsNames_IMDB.txt').itertuples():
        temp_aid = int(x[1][2:])
        if d_actors.get(temp_aid):
            d_actors[temp_aid]['name'] = x[2]
    with open('pickle_data/actors_pickle', 'wb') as f:
        pickle.dump(d_actors, f)
        del d_actors

    links = pd.read_csv('table_data/links_IMDB_MovieLens.csv', index_col='movieId')
    del links['tmdbId']
    links = links.to_dict('index')
    for x in pd.read_csv('TagScores_MovieLens.csv').itertuples():
        if x[3] > 0.5:
            temp_fid = links[x[1]]['imdbId']
            if d_films.get(temp_fid):
                temp_tid = x[2]
                d_films[temp_fid]['tags'].add(temp_tid)
                if d_tags.get(temp_tid):
                    d_tags[temp_tid]['films'].add(temp_fid)
                else:
                    d_tags[temp_tid] = {'name': '',
                                        'films': {temp_fid}}
    del links

    with open('pickle_data/films_pickle', 'wb') as f:
        pickle.dump(d_films, f)
        del d_films

    for x in pd.read_csv('table_data/TagCodes_MovieLens.csv').itertuples():
        temp_tid = x[1]
        if d_tags.get(temp_tid):
            d_tags[temp_tid]['name'] = x[2]

    with open('pickle_data/tags_pickle', 'wb') as f:
        pickle.dump(d_tags, f)


def load_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.MoviesSimular
    t_films, t_actors, t_tags = db.films, db.actors, db.tags
    with open('pickle_data/films_pickle', 'rb') as f:
        d_films = pickle.load(f)
    a = list(d_films.keys())
    for k in range(0, len(a), 80000):
        t_films.insert_many([{'_id': id,
                              'name': list(d_films[id]['name']),
                              'rate': d_films[id]['rate'],
                              'director': d_films[id]['director'],
                              'actors': list(d_films[id]['actors']),
                              'tags': list(d_films[id]['tags'])}
                             for id in a[k:k + 80000]])
    del d_films

    with open('pickle_data/actors_pickle', 'rb') as f:
        d_actors = pickle.load(f)
    a = list(d_actors.keys())
    for k in range(0, len(a), 80000):
        t_actors.insert_many([{'_id': id,
                               'name': d_actors[id]['name'],
                               'films': list(d_actors[id]['films'])}
                              for id in a[k:k + 80000]])
    del d_actors

    with open('pickle_data/tags_pickle', 'rb') as f:
        d_tags = pickle.load(f)
    t_tags.insert_many([{'_id': id,
                         'name': d_tags[id]['name'],
                         'films': list(d_tags[id]['films'])}
                        for id in d_tags])


if __name__ == '__main__':
    new_data_of_table = True
    new_data_to_db = True
    if new_data_of_table:
        load_dict_of_table()
    if new_data_to_db:
        load_db()
