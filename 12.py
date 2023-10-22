import matplotlib.pyplot as plt
import numpy as np

# Создание случайной матрицы 2x2
A = np.random.rand(2, 2)

# Вычисление собственных значений и собственных векторов
eigenvalues, eigenvectors = np.linalg.eig(A)

# Выбор двух неколлинеарных собственных векторов
v1 = eigenvectors[:, 0]
v2 = eigenvectors[:, 1]

# Создание графика
fig, ax = plt.subplots()

# Отображение векторов
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b')

# Установка пределов осей
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

# Отображение сетки
ax.grid(True)

# Отображение графика
plt.show()
