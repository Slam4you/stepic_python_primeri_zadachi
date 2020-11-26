import numpy as np


pyramid_osnovanie_lenght = np.array(input().split(), dtype=float)
pyramid_height = np.array(input().split(), dtype=float)
# 2a * sqrt( 0.25 a**2 + h**2) площадь боковая

v_max = np.max((1 / 3) * pyramid_osnovanie_lenght ** 2 * pyramid_height)
s_bok_min = np.min(2 * pyramid_osnovanie_lenght * np.sqrt(0.25 * pyramid_osnovanie_lenght ** 2 + pyramid_height ** 2))
V = np.where(pyramid_osnovanie_lenght == v_max)[0]
S = np.where(pyramid_height == s_bok_min)[0]
print("Vmax: %2d, %8.2f, Smin: %2d, %8.2f" % (V, v_max, S, s_bok_min))