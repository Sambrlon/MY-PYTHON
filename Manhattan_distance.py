# Манхэттенское расстояние

# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.

# На плоскости манхэттенское расстояние между двумя точками (p_{1}; \, p_{2})(p1​;p2​) и (q_{1}; \, q_{2})(q1​;q2​) определяется так |p_{1}-q_{1}|+|p_{2}-q_{2}|∣p1​−q1​∣+∣p2​−q2​∣.

# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

# Формат входных данных
# На вход программе подается четыре целых числа, каждое на отдельной строке – p_{1}, \, p_{2}, \, q_{1}, \, q_{2}p1​,p2​,q1​,q2​.

# Формат выходных данных
# Программа должна вывести одно число – манхэттенское расстояние.


p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

print(abs(p1 - q1) + abs(p2 -q2))


##### Другое решение


p1, p2, q1, q2 = [int(input()) for i in range(4)]
print(abs(p1 - q1) + abs(p2 -q2))