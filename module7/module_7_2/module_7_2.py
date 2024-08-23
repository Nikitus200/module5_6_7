def custom_write(file_name, strings):
    strings_positions = {}
    count_str = 1
    file = open(file_name, "w", encoding="utf-8")
    for i in strings:
        g = file.tell()
        dict_ = {(count_str, g): i}
        strings_positions.update(dict_)
        count_str += 1
        file.write(i + "\n")
    file.close()
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



