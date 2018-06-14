name = input('Введите ваше имя')
last_name = input('Введите вашу фамилию')
age = int(input('Введите ваш возраст'))
weight = int(input('Введите ваш вес'))
if age <= 30 and 50 <= weight <= 120:
    print(name, last_name, age, 'год', 'вес', weight, '- Хорошее состояние ')
elif age >= 40 and weight <= 50 or weight >= 120:
    print(name, last_name, age, 'год', 'вес', weight, '- Обратитесь к врачу')
elif age >= 30 and weight <= 50 or weight >= 120:
    print(name, last_name, age, 'год', 'вес', weight, '- Следует занятьс собой')
else:
    print(name, last_name, age, 'год', 'вес', weight, '- Есть к чему стримится')