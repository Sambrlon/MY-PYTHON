# for i in range(5):
#     n = int(input('Введите число: '))
#     print('Квадрат важего числа равен: ', n * n)
# print('Цикл завершен.')



# for i in range(11):
#     print(i)


# for i in range(10):
#     print(i + 1, '-- Привет')



# n = int(input())
# for i in range(n):
#     print('*' * (n - i))



m, p, n = int(input()), int(input()), int(input())

for i in range(n):
    print(i + 1, m)
    m = m + p/100*m
