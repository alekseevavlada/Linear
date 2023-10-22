import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# Входные данные - координаты вершин многоугольника
points = [
    [-2, 0],
    [0, 2],
    [2, 0],
    [0, -2]
]

# Матрица линейного отображения
matrix = np.array([
    [2, 0],
    [0, -1]
])

# Нахождение образов вершин многоугольника
transformed_points = np.dot(points, matrix.T)

# Создание графического изображения многоугольника на полученных вершинах
fig, ax = plt.subplots()
polygon = Polygon(transformed_points, closed=True, fc='blue', ec='black')
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
