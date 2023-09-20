import matplotlib.pyplot as plt

def plot_points(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.scatter(x, y, color='blue', zorder=2 )
    plt.xlabel('x')
    plt.ylabel('Y')
    plt.title('Plot of Points')

    plt.grid(True, zorder=1)

    plt.show()

points = [(0, 1), (3, 5), (9, 20), (15, 32)]
plot_points(points)
