import lesson05easy as easy
import os

def change_dir(dir_path):
    os.chdir(dir_path)
    return 'Вы перешли в папку: {}'.format(dir_path)
print('Вы находитесь в директории:', os.getcwd(), 'Вы можете:\n'
                                                  '1. Просмотреть содержимое текущей папки\n'
                                                  '2. Перейти в папку\n'
                                                  '3. Создать папку\n'
                                                  '4. Удалить папку\n')
answer = input('Выбирете действие: ')
if answer == '1':
    print(os.listdir())
elif answer == '2':
    dir_path = input('Укажите папку для перехода: ')
    print(change_dir(dir_path))
elif answer == '3':
    name = input('Введите имя папки: ')
    easy.make_dir_1(name)
elif answer == '4':
    name = input('Введите имя папки: ')
    easy.del_dir_2(name)