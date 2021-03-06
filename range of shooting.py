# Измерили дальности полета воды, выпущенной из шланга, под разными углами к горизонту.
# По этим данным построить тренд (полином второй степени) зависимости дальности полета от угла наклона шланга
# и найти дальность полета струи воды для произвольного угла.
# Входные данные:
# строка из целых чисел, разделенных пробелами, каждое значение - угол наклона шланга в градусах;
# строка из вещественных чисел, разделенных пробелами, каждое значение - дальность полета воды в метрах;
# угол наклона, для которого необходимо вычислить дальность (вещественное число).
# Выходные данные:
# дальность полета струи воды.
import numpy as np

def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y


angles = np.array(input().split(), dtype=int)
ranges = np.array(input().split(), dtype=float)
angle = float(input())
a = np.polyfit(angles, ranges, 2)
h_zero = get_trend(angle, a)
print("Дальность: %6.2f м" % (h_zero))

"""
27 34 41 48 55 62 69 76 83 90 97
75.23 95.49 98.03 89.5 84.57 82.07 69.58 48.82 26.36 0.0 -26.12
34
Sample Output:

Дальность:  89.19 м
"""
