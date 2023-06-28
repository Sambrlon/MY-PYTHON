# s = 'Полиморфизм'

# print(s[9])
# print(s[2])
# print(s[1])
# -----------------------------------

#s = 'Алиса привет'
# s = 'Улиса привет'

# if s[0] == 'А':
#     print('Первая буква - а')
# else:
#     print('Буква не начинается на - а')
# ---------------------------------

# s = 'Алиса привет'
# print(s[0:5])
# ---------------------------------

text = 'Алиса привет, как твои делишки?'

# if len(text) > 10:
#     print('Длина текста больше 10')
# if len(text) > 40:
#     print('Длина текста больше 40')
# --------------------------------

# my_str = 'Алиса привет, как твои делишки?'

# for i in my_str:
#     print(i)
# ---------------------------------

string = 'Алиса привет, как твои делишки?'

letters_count = 0
words_count = 0
spaces_count = 0

for letter in string:
    if letter not in [',', '.', '?', '!']:
        letters_count += 1
    elif letter == ' ':
        spaces_count += 1

if spaces_count > 0:
    words_count = spaces_count + 1
elif letters_count > 0:
    words_count += 1

print(f'Колличество букв - {letters_count}')
print(f'Колличество слов - {words_count}') 