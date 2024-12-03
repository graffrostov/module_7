import os
import time

# print(os.name)
# print(os.environ)
#
# print(os.getenv("TMP"))
# print(os.getcwd())

# print(os.path.exists(r'D:\Univer\module_7'))
# print(os.path.isfile(r"D:\Univer\module_7"))
# print(os.path.isdir(r"D:\Univer\module_7"))

# print('Текущая директория:', os.getcwd())
# создадим директорию и в ней файл.
# сменим рабочую директорию на вновь созданную
# потом не забудем всё это удалить


# if not os.path.exists('testdir'):
#     os.mkdir(r'testdir')
#     os.chdir(r'testdir')
#     os.mkdir(r'dir1')
#     os.mkdir(r'dir2')
#
# elif os.path.isdir('testdir'):
#   os.chdir(r'testdir')
#   if not os.path.exists('dir1'):
#     os.mkdir(r'dir1')
#
#   if not os.path.exists('dir2'):
#     os.mkdir(r'dir2')

# os.chdir('testdir')

print('Текущая директория:', os.getcwd())
# print('Список объектов:', os.listdir())

# Используем директорию проекта.
#
for root, dirs, files in os.walk('.'):

    for file in files:

        # для файла найдём относительный путь
        filepath = os.path.join(root, file)

        # получим последнее время записи файла
        filetime = os.path.getmtime(filepath)

        # приведём время к нормальному виду
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # получим размер файла
        filesize = os.path.getsize(filepath)

        # определим родительскую директорию относительно папки проекта
        parent_dir = os.path.dirname(filepath)

        # определим абсолютный путь
        parent_dir_abs = os.path.dirname(os.path.abspath(filepath))

        # выведем результат
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}, '
              f'Полный путь: {parent_dir_abs} ')
