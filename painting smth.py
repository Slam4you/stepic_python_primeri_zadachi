from matplotlib.patches import Wedge, Arc, PathPatch
import matplotlib.pyplot as plt


n = 6
m  = 5
plt.xlim(0, n)
plt.ylim(0,m)
ax = plt.gca()
plt.grid()

# нарисовать сектор
figure_w = Wedge((3, 1), 2, 45, 135)
ax.add_patch(figure_w)

# нарисовать дугу
# дуга должна иметь определенную толщину (linewidth = 3), нулевой угол поворота, цвет не указывать

figure_a = Arc((3, 1), 6, 6, 0, 45, 135, lw=3)
ax.add_patch(figure_a)


plt.show()