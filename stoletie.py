# Начало столетия

# Напишите программу, которая определяет, оканчивается ли год с 
# данным номером на два нуля. Если год оканчивается, то выведите «YES», 
# иначе выведите «NO».

# Формат входных данных
# На вход программе подаётся натуральное число.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

a = int(input())
b = a % 10
c = a % 100 // 10

if b == 0 and c == 0:
    print('YES')
else:
    print('NO')


##### Другое решение


a = int(input())
if a % 100 == 0:
    print("YES")
else:
    print("NO")



##### Другое решение


print('YES' if int(input()) % 100 == 0 else 'NO')