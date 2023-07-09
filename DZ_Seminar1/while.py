# answer = None

# while answer != 'пошли':
#     answer= input('Пошли тусить?: ')
# print('Я знал что ты согласишься!')



num = 4
is_solved = False

while not is_solved:
    ans = input('Угадай число: ')
    if int(ans) == num:
        print('Вы угадали!')
        is_solved = True
    else:
        print('Вы не угадали!')