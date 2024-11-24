import os

def custom_write(file_name, strings):
    string_positions = {}
    keys = []
    values = []
    if not os.path.isfile(file_name):
        file = open(file_name, 'w', encoding = 'utf-8')
        file.write(f'{strings[0]}\n')
        file = open(file_name, 'a', encoding='utf-8')
        for i in range (1, len(strings)):
            file.write(f'{strings[i]}\n')
    else:
        read = []
        with open(file_name, 'r', encoding = 'utf-8') as in_file:
            for s in (line.rstrip() for line in in_file.readlines()):
                read.append(s)
        if strings == read:
            pass
        else:
            file = open(file_name, 'a', encoding='utf-8')
            for i in strings:
                file.write(f'{i}\n')

    file = open(file_name, 'r', encoding = 'utf-8')
    key = (1, file.tell())
    keys.append(key)
    line_num = 2
    while line_num < len(strings) + 1:
        file.readline()
        key = (line_num, file.tell())
        keys.append(key)
        line_num += 1
    file.close()

    file = open(file_name, 'r', encoding='utf-8')
    lines = file.readlines()
    for i in range(len(lines)):
        values.append(lines[i].strip())
    file.close()

    string_positions = dict(zip(keys, values))

    return string_positions

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)

for item in result.items():
    print(item)
