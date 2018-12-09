from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.MoviesSimular
t_films = db.films
t_actors = db.actors
t_tags = db.tags


class TopN:
    def __init__(self, temp, n=10):
        self.arr = []
        for i in temp:
            while True:
                a = t_films.find_one({'name': i})
                if a and a not in self.arr:
                    self.arr.append(a)
                elif not a:
                    i = input(f'Название: {i} неверно или отсутвует в базе, '
                              f'попробуйте еще раз или нажмите Enter, чтобы пропустить:')
                    if i:
                        continue
                break

        temp = set(j for i in self.arr for j in self.all_simular(i))
        self._all = tuple(t_films.find_one({'_id': i}) for i in temp)
        self.top = (sorted(self._all,
                           key=lambda y: -sum((TopN.simular_film_rate(i, y) for i in self.arr)))
        [len(self.arr):n + len(self.arr)])

    def all_simular(self, x):
        ans = set()
        if x.get('director'):
            temp = t_actors.find_one({'_id': x['director']}) or {}
            ans.update(temp.get('films', set()))
        for i in x['actors']:
            temp = t_actors.find_one({'_id': i}) or {}
            ans.update(temp.get('films', set()))
        for i in x['tags']:
            temp = t_tags.find_one({'_id': i}) or {}
            ans.update(temp.get('films', set()))
        return ans

    def __str__(self):
        return ('Вы выбрали:\n' +
                '\n'.join(map(TopN._string, self.arr)) + '\n\n' +
                'Список похожих:\n' +
                '\n'.join(map(TopN._string, self.top)))

    @staticmethod
    def simular_film_rate(first, second):
        f1 = int(first['director'] == second['director']) * 0.1
        f2 = len(set(first['actors']) & set(second['actors'])) / len(first['actors']) * 0.2 if first['actors'] else 0
        f3 = len(set(first['tags']) & set(second['tags'])) / len(first['tags']) * 0.2 if first['tags'] else 0
        return (f1 + f2 + f3) + second['rate'] * 0.05

    @staticmethod
    def _get_persons_name(a, p=True):
        ans = []
        for i in a:
            if p:
                temp = t_actors.find_one({'_id': i}) or {}
            else:
                temp = t_tags.find_one({'_id': i}) or {}
            temp = temp.get('name')
            if temp:
                ans.append(temp)
        return ', '.join(ans)

    @staticmethod
    def _string(d):
        return (f'Название: {d["name"][0]}\n'
                f'Рейтинг: {d["rate"]}\n'
                f'Режиссер: {TopN._get_persons_name([d["director"]])}\n'
                f'Актеры: {TopN._get_persons_name(d["actors"])}\n'
                f'Теги: {TopN._get_persons_name(d["tags"], p=False)}\n')


if __name__ == '__main__':
    try:
        m, n = map(int, input().split())
        arr = tuple(input() for i in range(m))
        my_simular_top = TopN(arr, n)
        print(my_simular_top)
    except Exception as e:
        print(e)
