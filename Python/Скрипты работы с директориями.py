# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
print('Ваща текущая директория {}'.format(os.getcwd()))
def makedir(i):
    os.mkdir('{}'.format(i))
def removedir(i):
    os.rmdir('{}'.format(i))
def chdir(i):
    os.chdir(i)
for r in range(9):
    makedir('dir_{}'.format(r+1))
print(os.listdir())
for r in range(9):
    removedir('dir_{}'.format(r+1))

# Задача-2:
# Напишите скрипт отображающий папки текущей директории

def nowdir():
    print('Содержимое текущей папки: {}'.format(os.listdir()))

# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт

import shutil
shutil.copy('easy.py','easy_copy.py')