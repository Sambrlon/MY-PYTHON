# Наибольшее и наименьшее
# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

# Формат входных данных
# На вход программе подается пять целых чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.

# Тестовые данные 🟢
#     Номер теста    	    Входные данные    	    Выходные данные    
# 1	1
# 2
# 3
# 4
# 5	Наименьшее число = 1
# Наибольшее число = 5


a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))



##### Другое решение


nums = int(input()), int(input()), int(input()), int(input()), int(input())
print('Наименьшее число =', min(*nums))
print('Наибольшее число =', max(*nums))