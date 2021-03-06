# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

name = input('Введите ваше имя ')
sname = input('Введите вашу фамилию ')
email = input('Введите ваш email ')
nsnpat = '[А-ЯЁ][а-яё]+'
epat = '[a-z_0-9]+@[a-z]+\.(com|org|ru)'
try:
    if (re.match(nsnpat, name).group(0)) == name:
        print('Имя введено верно, спасибо')
except AttributeError:
    print('Вы где то ошиблись записывая имя. Попробуйте ещё раз!')

try:
    if (re.match(nsnpat, sname).group(0)) == sname:
        print('Фамилия введено верно, спасибо')
except AttributeError:
    print('Вы где то ошиблись записывая фамилию. Попробуйте ещё раз!')

try:
    if (re.search(epat,email).group(0)) == email:
        print('email введён верно, спасибо')
except AttributeError:
    print('Вы где то ошиблись записывая email. Попробуйте ещё раз!')

# Задача - 2:
# Вам дан текст:
# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

import re
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

pattern = '\.{2,}'
print((re.search(pattern,some_str)))
if (re.search(pattern,some_str)) is not None:
     print('В тексте есть многоточия')
else:
     print('В тексте нет многоточий')