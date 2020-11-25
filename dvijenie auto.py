import numpy as np
# Входные данные:
#
# строка, в которой через пробел перечислены длины всех участков дороги (целые числа);
# строка, в которой через пробел перечислены средние скорости на участках (целые числа);
# номер участка, на котором автомобиль въехал на дорогу (целое число);
# номер участка, после которого выехал (целое число).
# Выходные данные:
#
# длина пути с k по p участок;
# время в пути;
# средняя скорость движения автомобиля.

path = np.array(input().split(), dtype = int)
speed = np.array(input().split(), dtype = int)
k, p = int(input()), int(input())
len_path = np.sum(path)
len_path_k_to_p = np.sum(path[k: p + 1])
# print("Расстояние между пунктами А и В :", len_path)

time = path / speed
#  print("Время на каждом участке :", np.round(time, 2))

sum_time = time.sum()
sum_time_k_to_p = time[k: p + 1].sum()
# print("Общее время в пути : ", round(sum_time, 2))

avg_speed = len_path / sum_time
avg_speed_k_to_p = len_path_k_to_p / sum_time_k_to_p
# print("Средняя скорость : ", round(avg_speed, 2))

# Важно. Среднюю скорость нельзя вычислять как среднее значение скорости на всех участках!
# print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, sum_time, avg_speed))
print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path_k_to_p, sum_time_k_to_p, avg_speed_k_to_p))

