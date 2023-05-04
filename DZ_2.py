# Приветствуем пользователя

print('Првиет! Предлагаю проверить свои знания английского!')
user_name = input('Введите ваше имя: ')
print(f'Привет, {user_name}, начинаем тренировку!')

# Cчетчит правильных ответов.
right_answers = 0


# Начинаем задавать вопросы пользователю.
# Первый вопрос.
first_question = (f'My name ___{user_name}\n')
first_answer = 'is'
user_answer = input(first_question)
if user_answer == first_answer:
    right_answers += 1
    print('Ответ верный\nВы получили 10 баллов')
else:
    print(f'Неправильно. Правильный ответ: {first_answer}')

# Второй вопрос.
second_question = 'I ___ a coder\n'
second_answer = 'am'
user_answer = input(second_question)
if user_answer == second_answer:
    right_answers += 1
    print('Ответ верный\nВы получили 10 баллов')
else:
    print(f'Неправильно. Правильный ответ: {second_answer}')

# Третий вопрос.
third_question = 'I live ___ Moscow\n'
third_answer = 'in'
user_answer = input(third_question)
if user_answer == third_answer:
    right_answers += 1
    print('Ответ верный\nВы получили 10 баллов')
else:
    print(f'Неправильно. Правильный ответ: {third_answer}')

# Колличество баллов пользователя.
user_score = right_answers * 10

# Колличество процентов пользователя.
user_percentage = round((right_answers / 3) * 100, 2)

print(
    f'Тренировка завершена {user_name}!\n'
    f'Ты ответил на {right_answers} вопроса из 3 верно.\n'
    f'Ты заработал {user_score} баллов!\n'
    f'Это {user_percentage} процентов.\n'
)