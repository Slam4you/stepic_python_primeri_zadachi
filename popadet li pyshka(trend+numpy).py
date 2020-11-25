import numpy as np

# Создадим функцию для вычисления значений полинома второй степени в точке x, разместим ее в начале программы, после
# импорта модуля:
def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
# Входные данные:
#
# строка, в которой через пробел перечислены координаты движения снаряда по оси OX (вещественные числа);
# строка, в которой через пробел перечислены координаты движения снаряда по оси OY (вещественные числа);
# координаты мишени по оси ОХ;
# координаты мишени по оси OY.
# Выходные данные:
#
# высота, на которой стоит пушка
# yes или no в зависимости от того, попадет ли снаряд в мишень или нет.

x_array = np.array([255.7, 407.2, 559.2, 798.3, 820.5, 971.6, 1221.1, 1389.2])
h_array = np.array([256.9, 340.3, 390.3, 400.4, 397.1, 355.4, 213.5, 66.5])
x_target = 1380.4
h_target = 65.4
# x_array = np.array(input().split(), dtype = float)
# h_array = np.array(input().split(), dtype = float)
# x_target = float(input())
# h_target = float(input())

# Построим траекторию движения снаряда, используя в качестве линии тренда полином второй степени. Найдем его коэффициенты:
a = np.polyfit(x_array, h_array, 2)

# С помощью полученного тренда вычислим высоту, на которой находилась пушка. Значение координаты по оси ОХ в этой точке
# равно 0.
h_zero = get_trend(0, a)
print("Высота, на которой стоит пушка: %6.2f м" % h_zero)

# Вычислим, на какой высоте будет находиться снаряд в точке по оси ОХ, где расположена мишень
h_target_sharyada = get_trend(x_target, a)

print("Высота, в точке %4d м: %6.2f м" % (x_target, h_target))
# Определим, попадет ли снаряд в цель, если известно что мишень расположена на высоте 51 метр, учитывая, что радиус
# мишени 50 см =0.5 м. Для этого найдем модуль разности между высотой, на которой расположена мишень, и положением
# снаряда, вычисленного с помощью линии тренда. Затем сравним полученное значение с радиусом мишени и выведем результат.

delta_h = abs(h_target - h_target_sharyada)
if delta_h <= 0.5:
    print("Снаряд попадет в мишень.")
else:
    print("Снаряд не попадет в мишень.")