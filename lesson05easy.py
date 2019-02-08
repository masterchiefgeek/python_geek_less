import os
import shutil

# ДЗ к 5 уроку
#
#
# Задача №1

def make_dir():
    for i in range(1, 10):
        os.mkdir('dir_' + str(i))

def del_dir():
    for i in range(1, 10):
        os.rmdir('dir_' + str(i))


# Задача №2

print(os.listdir())


# Задача №3

def make_copy_file(current_file,copy_file):
    shutil.copy(current_file,copy_file)

current_file = os.path.abspath(__file__)
copy_file = current_file + '.copy'
make_copy_file(current_file,copy_file)



# Переработанные задания № 1 и 2 для использования в ДЗ normal
# где требуется вводить произвольные имена папок

def make_dir_1 (name):
    try:
        os.makedirs(name)
        print('Создана папка -', name)
    except FileExistsError:
        print('Папка', name, '- уже существует')

def del_dir_2 (name):
    try:
        os.rmdir(name)
        print('Удалена папка -', name)
    except FileNotFoundError:
        print('Папка', name, '- не существует')