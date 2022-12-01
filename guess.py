import random
n = random.randrange(1, 20)
guess = int(input('Введите любое число: '))
while n != guess:
    if guess < n:
        print('Слишком малое число')
        guess = int(input('Введите любое число снова: '))
    elif guess > n:
        print('Слишком большое число')
        guess = int(input('Введите любое число снова: '))
    else:
        break
print('Вы угадали верное число!')
