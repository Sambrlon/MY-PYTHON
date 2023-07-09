# 2. Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a = []
for _ in range(5):
    a.append(int(input('ведите число: ')))

max = a[0]
min = a[0]
min_i = 0
max_i = 0
avg = 0
for i in range(5):
    if a[i] > max:
        max = a[i]
        max_i = i

    if a[i] < min:
        min = a[i]
        min_i = i
    avg +=a[i]
print(f'max={max}')
print(f'min={min}')
print(f'max_i={max_i}')
print(f'min_i={min_i}')
print(f'Среднее={int(avg/5)}')