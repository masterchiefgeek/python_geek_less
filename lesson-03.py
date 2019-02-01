# УРОК №3

# Задания уровня easy
# Задание №1

def asl(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city) # Метод format оказался интересным для экспериментов
print(asl('Ратибор', 33, 'Муром'))


# Задание №2

def max_num (*args):
    return max(args)
print(max_num(10, -2, 3, 0))


# Задание №3

def max_sting(*args):
    return max(args, key = len)
print(max_sting('Hey there!', 'Tyger Tyger, burning bright,\nIn the forests of the night', 'Call +37 4952 125 21 23'))


# Задание уровня normal
# Задание №1

names = ['Anton', 'Ratibor', 'Borislav', 'Oleg', 'Alex', 'Dmitriy', 'Ivan', 'Miron']
salary =[270000, 300000, 100000, 510000, 200000, 75000, 250000, 300000]
salary_list = dict(zip(names, salary))
file = open('salary.txt', 'w', encoding='utf-8')
for x, y in salary_list.items():
    file.write('{} - {}\n'.format (x, y))
file.close()
file = open('salary.txt', 'r', encoding='utf-8')
for line in file:
    a = line.split(' - ')
    if int(a[1]) < 500000: # По логике не отображать людей получающих более зарплату 500000 относится только в выходным данным при чтении файлы.
        # У других пользователей условия чтения могут отличаться и они должны иметь полный файл.
        b = int(a[1])*0.87
    print('{} - {}'.format(a[0].upper(), b))
