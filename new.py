import matplotlib.pyplot as plt

v = [0.3, 1]
u = [-0.74, 1]

x = [0, v[0]]
y = [0, v[1]]

x2 = [0, u[0]]
y2 = [0, u[1]]

plt.plot(x, y, 'r', label='v1')
plt.plot(x2, y2, 'g', label='v2')

plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.legend()

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Vectors')

plt.show()
