import pymorphy2
from pymystem3 import Mystem
import os

morph = pymorphy2.MorphAnalyzer()
m = Mystem()

# text1 = open("1.txt").read().split()
# print(text1)
# text2
# text3
# text4
# text5

# text1 = list(text1.split())

PATH = "/Users/vladislavasan/PycharmProjects/python_classwork_1/the_village"


def openator(txt):
    f = open('{}.txt'.format(txt), "r")
    article = f.close()
    return article


def analizator():
    lst = os.listdir(PATH)
    for fl in lst:
        txt = openator(fl)
        analyzed = m.analyze(txt)
    print(analyzed[0]["analysis"][2]["gr"])


# p = morph.parse(text1)
# print(p)

# pos_count = 0
# if p.tag.POS:
#     pos_count += 1

analizator()
