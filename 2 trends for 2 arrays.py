import numpy as np

def get_trend1(x, a1):
    y = a1[0] * x + a1[1]
    return y
def get_trend2(x, a2):
    y = a2[0] * x**2 + a2[1] * x + a2[2]
    return y

# x_array = np.array(input().split(), dtype = float)
# h_array = np.array(input().split(), dtype = float)
x_array = np.array([-8.9, -8.5, -8.0, -7.1, -6.8, -6.1, -5.6, -5.5, -5.2, -5.2, -5.2, -4.2, -4.1, -3.5])
h_array = np.array([-1.4, -1.2, -1.1, -0.9, -0.8, -0.6, -0.5, -0.4, -0.3, -0.3, -0.3, -0.1, 0.1, 0.1])
a = np.polyfit(x_array, h_array, 1)
print("%5.3f %5.3f" % (a[0], a[1]))
a = np.polyfit(x_array, h_array, 2)
print("%5.3f %5.3f %5.3f" % (a[0], a[1], a[2]))
