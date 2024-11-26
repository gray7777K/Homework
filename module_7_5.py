import os
import time

os.chdir('test_dir')
print(os.getcwd())
directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, путь: {filepath}, размер: {filesize}, время изменения: {formatted_time}, родительская директория: {parent_dir}')
