# Пол и потолок

# Напишите программу, вычисляющее значение \lceil x\rceil + \lfloor x\rfloor⌈x⌉ +⌊x⌋ по заданному вещественному числу xx.

# Формат входных данных
# На вход программе подается одно вещественное число xx.

# Формат выходных данных
# Программа должна вывести одно число – значение указанного выражения.

# Примечание. \lceil x\rceil⌈x⌉ – потолок числа, \lfloor x\rfloor⌊x⌋ – пол числа.


from math import *
x = float(input())
print(floor(x) + ceil(x))
