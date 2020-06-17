# 1. Избавиться от предисловия
# 2. Показывать количество уникальных слов в каждом стихотворении
# 3. Частеречная структура
# 4. Есть ли в стихотворениях рифменные пары.

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from pymystem3 import Mystem
mystem = Mystem()


stops = set(stopwords.words('russian')) | {'gt', }
added_stops = {'весь', 'это', 'наш', 'оно', 'итак', 'т.п', 'т.е', 'мало', 'меньше', 'ещё', 'слишком', 'также',
                   'ваш', 'б', 'хм', 'который', 'свой', 'не', 'мочь', 'однако', 'очень', 'п', 'благодаря', 'кроме'}
stops = stops.union(added_stops)



reg_cyr = re.compile('[А-Яа-яЁё]')
cyr_vowels = re.compile('[АЯОЭЕЁУЮЫИаяоэеёуюыи]')
reg_title = re.compile('^[А-ЯA-Z .,!?-]+$')

class Poems:

    def __init__(self, poem_lines, title):
        self.lines = poem_lines
        if title != '* * *':
            self.title = title
        else:
            self.title = ''
        self.countLines()

    def countLines(self):

        def countWords(line):
            accents = 0
            words = line.split()
            for word in words:
                if word not in stops:
                    accents += 1
            return accents

        count_ln = 0
        syllabs = []
        words = []
        stanza = []
        stnz = 0
        mystemmed = []
        for line in self.lines:
            mystemmed.append(mystem.analyze(line))
            if not line:
                if stnz:
                    stanza.append(str(stnz))
                stnz = 0
            else:
                stnz += 1
            if not reg_cyr.search(line):
                continue
            count_ln += 1
            if count_ln == 1:
                if not self.title:
                    self.title = line
            syllabs.append(str(len(cyr_vowels.findall(line))))
            words.append(str(countWords(line)))
        self.count_ln = count_ln
        self.syllabs = syllabs
        self.words = words
        self.stanza = stanza
        self.mystemmed = mystemmed


txt_file = 'dom.txt'  # https://cloud.mail.ru/public/V2pn/2yB9UEnz2
with open(txt_file) as f:
    poem = []
    poems = []
    title = ''
    for line in f:
        line = line.strip()
        if '* * *' in line or reg_title.search(line):
            p = Poems(poem, title)
            poems.append(p)
            poem = []
            title = line
        else:
            poem.append(line)



with open(txt_file.replace('.txt', '_count.txt'), 'w') as fw:
    for p in poems[1:]:
        fw.write('\n\n{}\n'.format(p.title))
        fw.write('Длина в строках: {}\n'.format(p.count_ln))
        fw.write('Описание строфики: {}\n'.format('+'.join(p.stanza)))
        fw.write('Количество гласных в строках: {}\n'.format(', '.join(p.syllabs)))
        fw.write('Количество ударений в строках: {}\n'.format(', '.join(p.words)))
        fw.write(str(p.mystemmed))
