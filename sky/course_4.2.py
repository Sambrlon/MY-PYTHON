# Словари 4.2.2

# d = {}
# print(d)
#--------------------------------------------

# d = {'Лена': 3564774, 'Ваня': 7485853}
# print(d)
#--------------------------------------------

# d = dict(Лена=3564774, Ваня=7485853)
# print(d)

# dict - функция, которая создает словарь
#----------------------------------------

# d = dict(Лена=3564774, Ваня=7485853)
# print(d['Лена'])
#----------------------------------------

# explanation = {True: 'Да', False: 'Нет'}

# # print(explanation[3>2])

# if 3>2:
#     print(explanation[True])
# else:
#     print(explanation[False])
#----------------------------------------

# d = {'Число': 76348754, 'Строка': 'Ваня', 'Список': [1, 2, 3]}
# print(d)
#----------------------------------------

# dictionary = {'cat': 'Котейка'}

# print(dictionary)

# dictionary['dog'] = 'Собака'

# print(dictionary)

# dictionary['cat'] = 'Кошка' # Переписывает значение в словаре

# print(dictionary)

# del dictionary['cat'] # Удаляет значение из словаря

# print(dictionary)
#----------------------------------------

# dictionary = {
#     'cat': 'Котейка',
#     'dog': 'Собака',
#     'fish': 'Рыба',
#     'bird': 'Птица',
#     'хуй': 'Данил'
# }
# word = input('Введите слово: ')

# if word not in dictionary:
#     print('Такого слова нет в словаре')
# else:
#     translation = dictionary[word]
#     print(f'Первевод: {translation}')
#----------------------------------------

# 4.2.3 Словари изменение и добавление

# можем изменять значение. для этого пишем имя словаря,
# открываем квадратные скобки, указываем ключ словаря, затем после 
# знака присваивания указываем новое значение которое хотим присвоить ключу


# d = {'John': 'jogn@gmail.com', 'Kate': 'kate@gmail.com'}
# print(d)

# d['John'] = 'new_email.com'
# print(d)
#----------------------------------------

# del - оператор, который удаляет ключ\значение из словаря

# d = {'John': 'jogn@gmail.com', 'Kate': 'kate@gmail.com'}
# del d['Kate']
# print(d)
#----------------------------------------

# store = {'яблоки': 100, 'мандарины': 200, 'груши': 300}

# fruit = input('выберите фрукт: ')
# weight = int(input('выберите вес фрукта: '))

# price = store[fruit] * weight / 1000

# print(f'Стоимость: {price}')
#----------------------------------------

# 4.2.4 keys values items 

# d = {'John': 'jogn@gmail.com', 'Kate': 'kate@gmail.com'}

# for k in d:
#     print('Это ключ', k)
#     print('Это значение', d[k])
#----------------------------------------

# Чтобы при переборе циклом for получить ключи и значения словаря,
# нужно использовать метод items()

# d = {'John': 'jogn@gmail.com', 'Kate': 'kate@gmail.com'}
# for k, v in d.items():
#     print(f'это ключь {k}, это значение {v}')
# ----------------------------------------

# keys - чтобы получить все ключи словаря можно использовать метод keys()

# d = {'John': 'jogn@gmail.com', 'Kate': 'kate@gmail.com'}

# print(d.keys())

# for item in d.keys():
#     print(item)
#----------------------------------------

# d = {'John': 'jogn@gmail.com', 'Kate': 'kate@gmail.com'}

# print(d.values())

# for item in d.values():
#     print(item)
#----------------------------------------

# guests = {
#     'Karl': 1000,
#     'John': 2000,
#     'Kate': 3000,
#     'Bob': 4000,
# }

# guests_names = ', '.join(guests.keys())

# print(f'Список гостей: {guests_names}')

# total = 0

# for sum in guests.values():
#     total += sum

# print(f'Общая стоимость за дрочку каждому гостю: {total}')