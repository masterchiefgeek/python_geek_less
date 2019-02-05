# ДЗ №4
#
# Easy
#
# Задание №1

import random
my_lst = [random.randint(-10, 10) for i in range(15)]
print(my_lst, 'Исходный список')

squar_list = [i ** 2 for i in my_lst]
print(squar_list, 'Квадраты чисел исходного списка')


# # Задание №2

fruit_lst_1 = ['яблоко', 'груша', 'арбуз', 'слива', 'киви']
fruit_lst_2 = ['яблоко', 'банан', 'слива', 'явокадо', 'арбуз']
fruit_lst = [i for i in fruit_lst_1 if i in fruit_lst_2]
print(fruit_lst)
#
#
# # Задание №3

my_lst_2 = [i for i in my_lst if i % 3 == 0 and i >0 and i % 4 !=0]
print(my_lst_2, '\n Элемент кратен 3\n Элемент положительный\n Элемент не кратен 4')


# Normal
#
# Задание №1
import re

pattern_name_surname = '^[A-ZА-Я][a-zа-я]+$'
pattern_email = '^[a-z_0-9]+@[a-z0-9]+\.(ru|org|com)$'
while True:
    name = input('Введите Ваше имя: ')
    user_name = re.match(pattern_name_surname, name)
    if user_name:
        break
    else:
        print('Имя некорректно')
while True:
    surname = input('Введите Вашу фамилию: ')
    user_surname = re.match(pattern_name_surname, surname)
    if user_surname:
        break
    else:
        print('Фамилия некорректна')
while True:
    email = input('Введите Ваш email: ')
    user_email = re.match(pattern_email, email)
    if user_email:
        break
    else:
        print('email некорректен')


user_surname = re.match(pattern_name_surname, surname)
user_email = re.match(pattern_email, email)



# Задание №2

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

print('Текс содержит более одной точки' if re.search('\.{2,}', some_str) else 'Текст не содержит более одной точки')