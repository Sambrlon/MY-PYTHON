# Три города
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

# Примечание. Гарантируется, что длины названий всех трех городов различны.

# Тестовые данные 🟢
#     Номер теста    	    Входные данные    	    Выходные данные    
# 1	Москва
# Санкт-Петербург
# Екатеринбург	Москва
# Санкт-Петербург
# 2	Нью-Йорк
# Вашингтон
# Чикаго	Чикаго
# Вашингтон

a = input()
b = input()
c = input()

if min(len(a), len(b), len(c)) == len(a):
    print(a)
elif min(len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)
if max(len(a), len(b), len(c)) == len(a):
    print(a)
elif max(len(a), len(b), len(c)) == len(b):
    print(b)
else:
    print(c)


# Другое решение


a, b, c = str(input()), str(input()), str(input())
print(min(a, b, c, key=len ))
print(max(a, b, c, key=len ))