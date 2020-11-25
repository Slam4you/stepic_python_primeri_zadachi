import math as m
import numpy as np

# Дан многоугольник на плоскости, заданный  координатами своих вершин.
# Найти координаты вершин многоугольника, полученные поворотом каждой точки  на заданный угол вокруг начала координат.
# Вычислить средние значения координат по оси ОХ и ОУ повернутого многоугольника.

spot_list = []
n = int(input())    # кол-во вершин
for i in range(n):
    spot_list.append(input().split())
angle = int(input())
rotate_matr = [[m.cos(m.radians(angle)), m.sin(m.radians(angle))], [- m.sin(m.radians(angle)), m.cos(m.radians(angle))]]
rotate_matr = np.array(rotate_matr)
print(rotate_matr)
print()
spot_list = np.array(spot_list, dtype=int)
print(spot_list)
print()
rotated = np.dot(spot_list, rotate_matr)
print(rotated)
avg_x = np.average(rotated[:, 0])
avg_y = np.average(rotated[:, 1])
print("avg_x = %6.2f, avg_y=%6.2f" % (avg_x, avg_y))
