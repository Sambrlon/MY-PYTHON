# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.

# Формат входных данных
# На вход программе подаются три числа – длины сторон существующего треугольника.

# Формат выходных данных
# Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

# Тестовые данные 🟢
#     Номер теста    	    Входные данные    	    Выходные данные    
# 1	145
# 145
# 139	Равнобедренный
# 2	59
# 59
# 59	Равносторонний
# 3	890
# 199
# 700	Разносторонний
# 4	578930
# 694938
# 499093	Разносторонний
# 5	38876
# 38876
# 10	Равнобедренный
# 6	2002
# 2002
# 2002	Равносторонний
# 7	56
# 50
# 56	Равнобедренный
# 8	4
# 6
# 6	Равнобедренный

a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
elif a != b == c or a == b != c or a == c != b:
    print('Равнобедренный')
else:
    print('Разносторонний')


###########Другое решение

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')

###########Другое решение

a, b, c = int(input()), int(input()), int(input())
if a == b == c: print('Равносторонний')
elif a != b != c != a: print('Разносторонний')
else: print('Равнобедренный')

###########Другое решение

nums = set(int(input()) for _ in range(3))
print(["Равносторонний", "Равнобедренный", "Разносторонний"][len(nums) - 1])


###########Другое решение
a, b, c = int(input()), int(input()), int(input())
print(('Разносторонний', 'Равнобедренный', '', 'Равносторонний')[(a == b) + (a == c) + (b == c)])