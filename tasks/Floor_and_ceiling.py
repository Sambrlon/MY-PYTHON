# Пол и потолок

# Напишите программу, вычисляющее значение \lceil x\rceil + \lfloor x\rfloor⌈x⌉ +⌊x⌋ по заданному вещественному числу xx.

# Формат входных данных
# На вход программе подается одно вещественное число x.

# Формат выходных данных
# Программа должна вывести одно число – значение указанного выражения.



from math import *
x = float(input())
print(floor(x) + ceil(x))
