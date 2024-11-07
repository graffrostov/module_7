def custom_write(file_name, strings):

    strings_positions = {}
    number_str = 1

    work_file = open(file_name, 'w', encoding='utf-8')

    for item in strings:
        position = work_file.tell()
        strings_positions[(number_str, position)] = item
        work_file.write(f'{item}\n')
        number_str += 1

    work_file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)