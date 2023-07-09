# s = 'Полиморфизм'

# print(s[9])
# print(s[2])
# print(s[1])
# -----------------------------------

# s = 'Алиса привет'
# s = 'Улиса привет'

# if s[0] == 'А':
#     print('Первая буква - а')
# else:
#     print('Буква не начинается на - а')
# ---------------------------------

# s = 'Алиса привет'
# print(s[0:5])
# ---------------------------------

# text = 'Алиса привет, как твои делишки?'

# if len(text) > 10:
#     print('Длина текста больше 10')
# if len(text) > 40:
#     print('Длина текста больше 40')
# --------------------------------

# my_str = 'Алиса привет, как твои делишки?'

# for i in my_str:
#     print(i)
# ---------------------------------

# string = 'Алиса привет, как твои делишки?'

# letters_count = 0
# words_count = 0
# spaces_count = 0

# for letter in string:
#     if letter not in [',', '?', '!']:
#         letters_count += 1
#     elif letter == ' ':
#         spaces_count += 1

# if spaces_count > 0:
#     words_count = spaces_count + 1
# elif letters_count > 0:
#     words_count = 1

# print(f'Колличество букв - {letters_count}')
# print(f'Колличество слов - {words_count}') 
# --------------------------------

# email = 'lobinova@bk.ru'
# print(email.count('@')) 

# count - кол-во входжений
# ------------------------------------

# print('У меня в тексте есть Бльшие Буквы, А В ДРУГИХ НЕТ'.lower())

## .lower - метод для отображения слов в нижнем регистре
# ----------------------------------

# email = 'my new email lobinova@bk.ru'
# new_email = email.replace(' ', '_')
# print(new_email)
# print(email)

# .replace - заменяет все вхождения в строке на другую
# -----------------------------------

# 4.1.4

# Получить часть строки можно с методом split, является расзделителем строки
# -------------------------------

# s = 'Алиса привет, как твои делишки?'
# s = s.split(',')

# print(s)
# type(s)
#---------------------------------

# s = 'lobin@gmail.com'
# s = s.split('@')

# print(s)
# print(s[1])
#---------------------------------

# join - объединяет N строк в одну строку

# color = ['белый', 'красный', 'желтый']
# print(', '.join(color))
# print('.'.join(color))
# print('|'.join(color))
#---------------------------------

# message = '''
# Привет, мир! кто прившел изучить питон #добро пожаловать в чат!
# Тут будем общаться с @sambrlon'''

# people_mentioned = []
# tags_mentioned = []

# text = message.replace(',', '')

# words = text.split(' ')

# for word in words:
#     # if word[0] == '#':
#     if word.startswith('#'):
#         tags_mentioned.append(word)
#     elif word.startswith('@'):
#         people_mentioned.append(word)

# people_mentioned_joined = ' '.join(people_mentioned)
# tags_mentioned_joined = ' '.join(tags_mentioned)

# print(f'Упомянутые люди: {people_mentioned_joined}')
# print(f'Упомянутые теги: {tags_mentioned_joined}')
#---------------------------------


