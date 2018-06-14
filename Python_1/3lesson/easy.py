# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

name, age, city = (input('Введите ваше имя, возраст и город проживание: ').split( ))
def inf (*agrs):
    return (f'{name}, {age} года(а), проживает в городе {city}')
print(inf(name, age, city))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
list = (int (i) for i in input('Введите числа через пробел ').split())
def max (args):
    counter = 0
    for i in list:
        if i > counter:
            counter = i
    return counter
print (max(list))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def lenght(args):
    counter = 0
    string = 0
    for i in args:
        if len(i) > counter:
            counter = len(i)
            string = (i)
    return (string)
