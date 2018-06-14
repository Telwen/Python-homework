# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
#
# for c in range(10):
#     if c > 0:
#         os.mkdir('dir_' +str(c))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import sys

# print(sys.argv)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import codecs
way = sys.argv
filename = []
for args in way:
    filename.append(args.split('/'))

with open(os.getcwd() + '/' + filename[0][-1], 'r',encoding='utf-8') as corf:
    with open(os.getcwd() + '/' + 'copy_of_' + filename[0][-1], 'w', encoding='utf-8') as wrf:
        for str in corf:
            wrf.write(str)