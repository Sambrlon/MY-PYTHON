# Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def inputKoord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f'Введите {i + 1} число: '))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print('Координата не должна быть равной 0!')
            except ValueError:
                print('Ошбика, введите число!')
    return a

def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    elif xy[0] > 0 and xy[1] < 0:
        text = 4
    print(f'Точка находится в {text} четверти плоскости.')

koordinate = inputKoord(2)
checkCoordinates(koordinate)