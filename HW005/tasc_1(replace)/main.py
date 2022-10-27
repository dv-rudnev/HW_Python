# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def write_file(name, data):
    '''Перезаписывает данные в файл. Если файл отсутствует, создает его.
    Принимает имя файла (name) и данные (data)'''
    with open(name, 'w', encoding='utf-8') as f:
        f.write(data)

        
from_keyboard = input('\nВведите слова через пробел: ')

file_name = 'from_keyboard.txt'
write_file(file_name, from_keyboard)
print(f'\n---Создали файл {file_name}. Все сохраннено в нем.\n')

sub_str = input('Теперь удалим слова содержащие определенное буквосочетание.\nВведите словосочетание: ')

with open(file_name, 'r', encoding='utf-8') as f:
    from_file = f.read().split()
    # filtered = ' '.join(filter(lambda x: sub_str not in x, f.read().split()))

filtered = ' '.join(filter(lambda x: sub_str not in x, from_file))
new_file_name = 'filtered.txt'
write_file(new_file_name, filtered)
print(f'\nИз введенных слов: {from_keyboard}, удалено все содержащее {sub_str}.\nОставшиеся слова: {filtered}, сохранены в файл: {new_file_name}')
