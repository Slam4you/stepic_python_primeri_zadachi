# Трое сотрудников получили премию в размере 2970 р., причем второй получил 1/3 того, что получил первый,
# и еще 180 р., а третий получил 1/3 денег второго и еще 130 р. Какую премию получил каждый?
import numpy as np
import numpy.linalg as alg

a_list = [1, 1, 1], [-1/3, 1, 0], [0, -1/3, 1]
a_list = np.array(a_list, dtype=float)
b_list = [2970, 180, 130]
b_list = np.array(b_list, dtype=float)
x = np.dot(alg.inv(a_list), b_list)
print("%4d р., %4d р., %4d р." % (x[0], x[1], x[2]))

