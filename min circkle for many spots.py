# Даны n точек на плоскости найти центр и минимальный радиус круга, куда попадут все эти точки.
import math as m
import numpy as np


def lenght_from_to(x_a, y_a, x_b, y_b):
    return(m.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2))


spot_list = []
n = int(input())    # кол-во точек
for i in range(n):
    spot_list.append(input().split())
spot_list = np.array(spot_list, dtype=float)
avg_x = np.average(spot_list[:, 0])
avg_y = np.average(spot_list[:, 1])
print(avg_x, avg_y)
max_radius_list = []
for i in spot_list:
    max_radius_list.append(lenght_from_to(i[0], i[1], avg_x, avg_y))
print(max_radius_list)
print("О(%6.3f, %6.3f), r = %6.3f" % (avg_x, avg_y, max(max_radius_list)))

"""import numpy as np
points = np.array([input().split() for _ in range(int(input()))], dtype=float)
average = np.mean(points,0)
X2 = (points[:,0] - average[0]) ** 2
Y2 = (points[:,1] - average[1]) ** 2
dist = np.sqrt(X2 + Y2)
r = np.max(dist)
print("О(%6.3f, %6.3f), r = %6.3f" % (average[0],average[1],r))"""