from settings import *


def line(u):
    return u


def poly2(u):
    return u ** 2


def grid(f, x0, x1, n, args=()):

    dx = (x1 - x0) / n
    nodes = []
    for i in range(n+1):
        nodes.append(f(x0 + i * dx, *args))
    return nodes

if __name__ == "__main__":

    # Mesh settings 
    u0, u1, n = 0, 4, 10
    x = grid(poly2, u0, u1, n)
    y = np.zeros(shape=(n+1,))

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.grid(True)

    plt.show()
