import os
import re


def readfile(txt):
    f = open('{}.txt'.format(txt), "r")
    novel = f.read()
    f.close()
    return novel.replace('\n', '')


def find_reg(regexp, txt):
    what = readfile(txt)
    result = re.findall(regexp, what)
    return result


def find_in_txt():
    structure = open("test/structure_war_and_peace.txt", "w+")
    novel = ['war_and_peace']
    for volume in novel:
        structure.write(str(find_reg("Лев\sНиколаевич\sТолстой\.\sВойна\sи\sмир\.\s+(Том\s\d+)", volume)))
    for part in novel:
        structure.write(str(find_reg("\*\sЧАСТЬ\s*([А-Я]*)\.\s\*", part)))
    for chapter in novel:
        structure.write(str(find_reg("\s+([IVXL])+\.", chapter)))

    structure.close()

find_in_txt()

#
#
# def final():
#     for root, dirs, files in os.walk(path):
#         for fl in files:
#             f = open("{}/{}".format(root, fl) + find("\*\sЧАСТЬ\s*([А-Я]*)\.\s\*"))
#
#     for co in countries:
#         result.write(
#             "Cтолица {}".format(co) + ' ' + find("title=\"Столица\".*([А-Я][а-я]*)</a></span></td>", co) + '\n')
#     result.close()

# Вариант решения:
# re.sub("глава([0-9]+)", "\1+++---+++", text)
# chapters = text.split("+++---+++")
# text = re.sub('(о)п(а)', r"\2п\1")
# \\1 \\2