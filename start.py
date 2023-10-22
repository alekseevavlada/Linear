import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Координаты вершин ромба
points = [
    [-2, 0],
    [0, 2],
    [2, 0],
    [0, -2]
]

# Создание графического изображения ромба на вершинах
fig, ax = plt.subplots()
polygon = Polygon(points, closed=True, fc='blue', ec='black')
ax.add_patch(polygon)
ax.set_aspect('equal', 'box')
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid(True)
plt.show()
