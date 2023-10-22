import numpy as np
import matplotlib.pyplot as plt

# Создаем массив x, представляющий все возможные значения x на плоскости
x = np.linspace(-10, 10, 100)

# Создаем прямую y=2x
y = 2 * x

# Задаем координаты точки
point_x = 1
point_y = 3

# Отображаем прямую и точку
plt.plot(x, y, label='y=2x')
plt.scatter(point_x, point_y, color='red', label='Исходная точка')

# Вычисляем координаты отраженной точки
reflected_x = -3/5 * point_x + 4/5 * point_y
reflected_y = 4/5 * point_x + 3/5 * point_y

# Отображаем отраженную точку
plt.scatter(reflected_x, reflected_y, color='green', label='Отраженная точка')

# Добавляем оси координат и метки
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')

# Устанавливаем пределы осей координат
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Добавляем легенду
plt.legend()

# Отображаем график
plt.show()
