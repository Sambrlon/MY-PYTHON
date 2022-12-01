# Среднее число
# Даны три различных целых числа. Напишите программу, 
# которая находит среднее по величине число.

# Формат входных данных
# На вход программе подаётся три различных целых числа, 
# каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести среднее число.

# Примечание. Средним называется число, которое будет вторым, 
# если три числа отсортировать в порядке возрастания.

# Тестовые данные 🟢
#     Номер теста    	    Входные данные    	    Выходные данные    
# 1	1
# 2
# 3	2
# 2	10
# 30
# 20	20
# 3	67
# 100
# 54	67
# 4	54
# 34
# # 33	34

a, b, c = int(input()), int(input()), int(input())
if a < b < c or a > b > c:
    print(b)
elif b < c < a or b > c > a:
    print(c)
else:
    print(a)


###########Другое решение

a = int(input())
b = int(input())
c = int(input())
if b<a<c or c<a<b:
    print(a)
elif a<b<c or c<b<a:
    print(b)
else:
    print(c)