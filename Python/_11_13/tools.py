import json
import os
from difflib import SequenceMatcher

import requests
from bs4 import BeautifulSoup


########################################################################################################################

def _text_transform(s):
    return s.get_text().strip()


########################################################################################################################

class MyException(Exception):
    def __init__(self):
        pass


class NoHaveInternet(MyException):
    def __init__(self):
        pass

    def __str__(self):
        return (f'Ошибка: Не обнаружено интернет соединение, попытайтесь восстановить его\n'
                f'Чтобы попытаться еще раз[L], завершить работу[E]')


class NoHaveSite(MyException):
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return (f'Ошибка: {self.count} сайтов не нашлось. '
                f'Хотите продолжить[C] или попытаться загурзить нужные сайты еще раз[L]')


class NoHaveSiteDescribe(MyException):
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return (f'Ошибка: {self.count} у стольких сайтов не нашлось описания. '
                f'Хотите продолжить[C] или попытаться загурзить сайты с нужным описанием еще раз[L]')


class FileNoExist(MyException):
    def __init__(self):
        pass

    def __str__(self):
        return (f'Ошибка: Файла для записи с таким именем не существует. '
                f'Чтобы ввести верное название файла[F], создать файл для записи с нужным именем[N], '
                f'завершить работу[E]')


########################################################################################################################

class Factory:
    def __init__(self, app=True, load=False, count=1000, debug=False):
        self._app = app
        self._load = load
        self._debug = debug
        self._write_count = count
        self.jokes_file = 'jokes.txt'
        self.jokes_json_file = 'jokes_json.txt'
        self.result_file = 'result.txt'
        self.url_site_news = r'http://static.feed.rbc.ru/rbc/logical/footer/news.rss'
        self._run()

    def _run(self):
        try:
            if self._load:
                self._jokes()
                self._load = False
            if self._app:
                self._news()
                self._app = False
        except MyException as e:
            print(e)
            flag = input()
            if flag == 'L':
                self._run()
            if flag in ('F', 'N'):
                self.jokes_json_file = input()
                self.jokes_file = input()
                self.result_file = input()
                if flag == 'N':
                    f1 = open(self.jokes_json_file, 'a')
                    f2 = open(self.jokes_file, 'a')
                    f3 = open(self.result_file, 'a')
                    f1.close()
                    f2.close()
                    f3.close()
                self._run()

    def _jokes(self):
        error1 = error2 = 0
        num = 453082
        for num in range(num, num - self._write_count, -1):
            url = f'https://bash.im/quote/{num}'
            try:
                joke_ = Joke(url, self._debug)
                if joke_.descr:
                    joke_.save(self.jokes_file)
                    joke_.to_JSON(self.jokes_json_file)
                else:
                    raise NoHaveSiteDescribe
            except NoHaveSiteDescribe:
                error1 += 1
                continue
            except ConnectionError:
                error2 += 1
                continue
        if error2 == self._write_count:
            raise NoHaveInternet()
        if error1 != 0:
            raise NoHaveSiteDescribe(error1)
        if error2 != 0:
            raise NoHaveSite(error2)

    def _news(self):
        counter = error = 0
        try:
            news_sites = self._parse_rss()
        except Exception:
            raise NoHaveInternet()
        for url in news_sites:
            try:
                counter += 1
                new_ = New(url, self._debug)
                if new_.name and new_.p1 and new_.descr:
                    new_.find_(self.jokes_file)
                    new_.save(self.result_file)
            except ConnectionError:
                error += 1
        if counter == error != 0:
            raise NoHaveInternet()
        if error != 0:
            raise NoHaveSite(error)

    def _parse_rss(self):
        answer = []
        html = requests.get(self.url_site_news).text
        html = html.replace('windows-1251', 'utf-8', 1)
        soup = BeautifulSoup(html, features='lxml-xml')
        for x in soup.find_all('link'):
            x = _text_transform(x)
            if x not in (r'https://www.rbc.ru/', '',):
                answer.append(x)
        return answer


########################################################################################################################

class Joke:
    def __init__(self, url, debug):
        self._debug = debug
        self._html = requests.get(url).text
        self._soup = BeautifulSoup(self._html, features='lxml')
        self._get_description()

    def _get_description(self):
        try:
            x = self._soup.find('div', {'class': 'text'})
            self.descr = _text_transform(x)
        except Exception:
            raise NoHaveSiteDescribe

    def save(self, file_):
        if not os.path.isfile(file_):
            raise FileNoExist
        with open(file_, mode='a', encoding='utf-8') as f:
            if not self._debug:
                f.write(f'{self.descr}\n')
            else:
                print(self.descr)

    def _default(self, instance):
        return {k: v
                for k, v in vars(instance).items()
                if not str(k).startswith('_')}

    def to_JSON(self, file_):
        if not os.path.isfile(file_):
            raise FileNoExist
        with open(file_, mode='a', encoding='utf-8') as f:
            x = json.dumps(self, default=self._default)
            x = f'{x}\n\n\n'
            if not self._debug:
                f.write(x)
            else:
                print(x)


########################################################################################################################

class New:
    def __init__(self, url, debug):
        self._debug = debug
        self.url = url
        self._html = requests.get(url).text
        self._soup = BeautifulSoup(self._html, features='lxml')
        self._get_name()
        self._get_description_and_p1()

    def _get_name(self):
        try:
            x = self._soup.find('div', {'class': 'article__header__title'})
            self.name = _text_transform(x)
        except Exception as e:
            raise NoHaveSiteDescribe

    def _get_description_and_p1(self):
        self.descr = ''
        self.p1 = ''
        try:
            for k, x in enumerate(self._soup.find('div', {'class': 'article__text'}).find_all('p'), start=1):
                if k == 1:
                    self.p1 = _text_transform(x)
                self.descr += _text_transform(x)
        except Exception:
            raise NoHaveSiteDescribe

    def find_(self, file_, limit=1000):
        if not os.path.isfile(file_):
            raise FileNoExist
        self.simular_joke = ''
        comp = SequenceMatcher(a=self.descr, b=self.descr)
        mx = 0
        with open(file_, mode='r', encoding='utf-8') as f:
            for ind, joke in enumerate(f, start=1):
                comp.set_seq2(joke)
                temp = comp.ratio()
                if temp > mx:
                    mx = temp
                    self.simular_joke = joke
                if ind == limit:
                    break

    def save(self, file_):
        if not os.path.isfile(file_):
            raise FileNoExist
        with open(file_, 'a', encoding='utf-8') as f:
            s = (f'Заголовок новости: {self.name}\n'
                 f'Ссылка на новсоть: {self.url}\n'
                 f'Первый параграф: {self.p1}\n'
                 f'Шутка: {self.simular_joke}\n\n\n')
            if not self._debug:
                f.write(s)
            else:
                print(s)
