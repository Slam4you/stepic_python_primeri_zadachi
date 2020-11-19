import matplotlib.pyplot as plt
import math as m


def compute_population(t):
    popul = (172 / 45) * ((m.pi / 2) - m.atan((2000 - t) / 45))
    return popul


line = "2164 2169"
years_str_list = line.split()
years_list = [int(i) for i in line.split()]
population_list = [compute_population(t) for t in years_list]

for i in range(len(years_list)):
    print("%5d - %6.3f миллиард(ов)" % (years_list[i], population_list[i]))


x_list = [years_list[0], years_list[1]]
y_list = [population_list[0], population_list[1]]

plt.gca().spines["left"].set_position("center")

plt.gca().spines["bottom"].set_position("center")
plt.plot(x_list, y_list)
#plt.show()

# Задача!
# Входные данные:
#
#  два целых числа, соответствующие первому и последнему индексам списков, для которых нужно произвести вычисления.
# Например, на входе программы числа 3 и 7. Это значит, что вычисления нужно произвести для списков, состоящих из
# элементов исходных списков с номерами 3, 4, 5, 6 и 7. Выделить эти элементы из, например, списка years можно с
# помощью среза years[3:8].
#
# Выходные данные:
#
# год, в котором погрешность между реальной и вычисленной численностью минимальна (целое число);
# год, в котором погрешность между реальной и вычисленной численностью максимальна (целое число);
# средняя погрешность в процентах (вещественное число).

years = [1000, 1750, 1800, 1850, 1900, 1950, 1955,
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995,
         2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]

population =[0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
             2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
             5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
             7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]

y1, y2 = 7, 26

new_year_list = [int(i) for i in years[y1:y2 + 1]]
new_population_list = [float(i) for i in population[y1:y2 + 1]]
new_compute_population_list = [compute_population(t) for t in new_year_list]
new_error_list = [abs((new_population_list[i] - new_compute_population_list[i]) / new_population_list[i])
                  for i in range(len(new_population_list))]
print(new_compute_population_list)
print(new_error_list)
pogr_min = new_year_list[new_error_list.index(min(new_error_list))]
pogr_max = new_year_list[new_error_list.index(max(new_error_list))]
avg_error = (((sum(new_error_list) / len(new_compute_population_list)) * 100))
print(avg_error)

print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f" % (pogr_min, pogr_max, avg_error))

