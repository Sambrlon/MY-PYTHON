# Евклидово расстояние
# На плоскости евклидово расстояние между двумя точками (x_{1}; \, y_{1})(x 
# 1
# ​
#  ;y 
# 1
# ​
#  ) и (x_{2}; \, y_{2})(x 
# 2
# ​
#  ;y 
# 2
# ​
#  ) определяется так \rho = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}ρ= 
# (x 
# 1
# ​
#  −x 
# 2
# ​
#  ) 
# 2
#  +(y 
# 1
# ​
#  −y 
# 2
# ​
#  ) 
# 2
 
# ​
#  .



# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

# Формат входных данных
# На вход программе подается четыре вещественных числа, каждое на отдельной строке – x_{1}, \, y_{1}, \, x_{2}, \, y_{2}x 
# 1
# ​
#  ,y 
# 1
# ​
#  ,x 
# 2
# ​
#  ,y 
# 2
# ​
#  ​.

# Формат выходных данных
# Программа должна вывести одно число – евклидово расстояние.

# Тестовые данные 🟢
#     Номер теста    	    Входные данные    	    Выходные данные    
# 1	2.0
# 2.5
# 44.155
# 100.50	106.68197610187018
# 2	5.5
# 2.4
# 4.9
# 6.3	3.9458839313897713


import math
x1, x2, y1, y2 = float(input()), float(input()), float(input()), float(input())
print(math.hypot(x1 - y1, x2 - y2))