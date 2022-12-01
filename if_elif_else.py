# Задача 1. Даны три целых числа. Определите, 
# сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 
# (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# 1 способ. Использование вложенного условного оператора.

a, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)


# 2 способ. Использование каскадного условного оператора.

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b == c:
    print(2)
elif a == c != b:
    print(2)
else:
    print(0)

# 3 способ. 
# Использование каскадного условного оператора и логического оператора or.

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c or a != b == c or a == c != b:
    print(2)
else:
    print(0)
