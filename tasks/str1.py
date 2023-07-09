# апишите программу, которая выводит текст:

# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

# Примечание. Используйте конкатенацию строк.

# Тестовые данные 🟢
# Sample Input:

# Sample Output:

# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."


a = '"Python is a great language!", said Fred. '
b = '"I don'
c = "'t ever remember having this much "
d = 'fun before."'
print(a + b + c + d)


# Другое решение

print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')