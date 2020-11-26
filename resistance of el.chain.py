# Входные данные:
#
# строка, в которой через пробелы перечислены значения сопротивления на каждом резисторе (вещественные числа);
# строка, в которой через пробелы перечислены значения силы тока на каждом резисторе (вещественные числа).
# Выходные данные:
#
# значение общего сопротивления цепи;
# сила тока;
# напряжение.

import numpy as np

r_list = input().split()
i_list = input().split()
i_list = np.array(i_list, dtype=float)
r_total_reversed = 0
for i in range(len(r_list)):
    r_total_reversed += 1 / float(r_list[i])
r_total = 1 / r_total_reversed
i_total = np.sum(i_list)
u_total = i_total * r_total
print("R = %6.3f Ом, I = %6.3f А, U = %6.3f В" % (r_total, i_total, u_total))

"""
import numpy as np
r, i = np.array(input().split(), dtype=float), np.array(input().split(), dtype=float)
print(f'R = %6.3f Ом, I = %6.3f А, U = %6.3f В' % (1/sum(1/r), np.sum(i), np.sum(i)/sum(1/r)))
"""