# Ход ферзя
# Даны две различные клетки шахматной доски. 
# Напишите программу,  которая определяет, может ли ферзь попасть с 
# первой клетки на вторую одним ходом. Программа получает на вход 
# четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки 
# сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести «YES», если из первой клетки ходом 
# ферзя можно попасть во вторую или «NO» в противном случае.

# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Шахматный ферзь ходит по диагонали, горизонтали или вертикали.



# Тестовые данные 🟢
#     Номер теста    	    Входные данные    	    Выходные данные    
# 1	                              1
#                                 1
#                                 2
#                                 2	                     YES
# 2	1
#   1
#   2
#   3	                                                  NO
# 3	5
#   6
#   3
#   3	                                                  NO



x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


##### Другое решение

