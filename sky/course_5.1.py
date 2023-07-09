# 5.1.2
# метод randint - выдает любую случайную цифру из диапазона

# import random
# print('Вывод случайного числа', random.randint(1,100))
#-------------------------------------------

# from random import randint
# print('Вывод случайного числа', randint(1, 100))
#-------------------------------------------


# random.shuffle - перемешивает список

# import random 
# my_list = [2, 5, 8, 9, 12]
# print('Список до перемешивания', my_list)

# random.shuffle(my_list)
# print('Список после перемешивания', my_list)
#-------------------------------------------

# random.sample - выбирает случайное число из списка по диапазону

# import random

# name = 'Алиса'

# items = random.sample(name, 3)
# result = ''.join(items)
# print(result)
#-------------------------------------------

# import random

# gifts = ['яблоки', 'мандарины', 'груши', 'бананы', 'персик']

# index = random.randint(0, len(gifts) - 1)
# gift = gifts[index]

# random.shuffle(gifts)
# gift = gifts[0]

# gift = random.sample(gifts, 1)[0] # пишем индекс чтобы вытащить из списка первый элемент

# print(f'Вы выиграли {gift}')
#-------------------------------------------

# 5.1.3

# def alfa_tango():
#     my_str = 'Papa Yankee Tango Hotel Oscar Nord'
#     list_str = my_str.split()
#     print(list_str)

#     new_str = ''
#     for word in list_str:
#         new_str +=word[0]
#     print(new_str)

# alfa_tango()
#-------------------------------------------

# import random 

# def random_gift():
#     gifts = ['яблоки', 'мандарины', 'груши', 'бананы', 'персик']

#     random.shuffle(gifts)
#     gift = gifts[0]

#     print(f'Вы выиграли {gift}')

# while True:
#     input()
#     random_gift()
#-------------------------------------------

# 5.1.4





