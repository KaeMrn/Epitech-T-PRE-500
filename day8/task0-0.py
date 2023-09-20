import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [12, 32, 42, 52]

plt.scatter(x, y, color='red', zorder=2)
plt.ylabel('some numbers')
plt.grid(True, zorder=1)
plt.show()
