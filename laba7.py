from math import sqrt
print ("Введите 1 для расчета через длины сторон, или 2 расчета по координатам")
n = float(input())
if n == 1:
    print("введите длины сторон")
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    p = (a + b + c) / 2.0  # Полупериметр
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("S = {}".format(S))
elif n == 2:
    print("Введите координаты первой вершины")
    x1, y1 = map(float, input().split())
    print("Введите координаты второй вершины")
    x2, y2 = map(float, input().split())
    print("Введите координаты третьей вершины")
    x3, y3 = map(float, input().split())
    a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    p = (a + b + c) / 2.0
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print('S =', "%.04f" % s)
elif n != 1 and n != 2:
    print("Введите 1 или 2!")




