# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("make_dir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def ls():
    way = os.getcwd()
    print(way)

def cd():
   if sys.argv[2] in os.listdir():
       os.chdir(os.getcwd() + '/' + sys.argv[2])
   else:
       os.chdir(sys.argv[2])

def rm():
    print('Вы уверены, что хотите удалить папку безвозвратно? (Введите 1, если да, 0, если нет.')
    des = int(input())
    if des == 1:
        if sys.argv[2] in os.listdir():
            os.removedirs(os.getcwd() + '/' +(sys.argv[2]))

def ping():
    print("pong")

def cp():
    filename = sys.argv[2]
    directory = os.listdir()
    if filename in directory:
        with open(os.getcwd() + '/' + filename, 'r', encoding='utf-8') as corf:
            with open(os.getcwd() + '/' + 'copy_of_' + filename, 'w', encoding='utf-8') as wrf:
                for str in corf:
                    wrf.write(str)
    else:
        print('Такой файл не существует или вы ввели имя неправильно. Попробуйте ещё раз')


do = {
    "help": print_help,
    "make_dir": make_dir,
    "ping": ping,
    "cp": cp,
    "ls": ls,
    "cd": cd,
    "rm": rm
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
print("Укажите ключ help для получения справки")