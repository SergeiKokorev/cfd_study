from settings import *


def ctop(u, y):
    return np.array([2 * u, 0 * u + y, u ** 2])


def cleft(v):
    return np.array([0 * v, 2 * v, v ** 2])


def cright(v, x):
    return np.array([0 * v + x, 2 * v, v ** 2])


def cbot(u):
    return np.array([2 * u, 0 * u, u ** 2])


def parameter(n):
    return np.array([(i - 1) / (n - 1) for i in range(1, n + 1)])


def tfi_grid(ftop, fbot, fleft, fright, u, v, *, atop=(), abot=(), aleft=(), aright=()):

    ni, nj = u.size, v.size
    x = np.zeros(shape=(ni, nj, 3))
    
    for i in range(ni):
        for j in range(nj):
            x[i, j] = (1 - v[j]) * fbot(u[i], *abot) + v[j] * ftop(u[i], *atop) + \
            (1 - u[i]) * fleft(v[j], *aleft) + u[i] * fright(v[j], *aright) - \
            (u[i] * v[j] * ftop(u[-1], *atop) + u[i] * (1 - v[j]) * fbot(u[-1], *abot) + \
            v[j] * (1 - u[i]) * ftop(u[0], *atop) + (1 -u[i]) * (1 - v[j]) * fbot(u[0], *abot))

    return x


if __name__ == "__main__":
    
    ni, nj = 25, 25
    u, v = parameter(ni), parameter(nj)
    nodes = tfi_grid(ctop, cbot, cleft, cright, u, v, aright=[4], atop=[4])
    x, y, z = nodes[:,:,0], nodes[:,:,1], nodes[:,:,2]

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, y, z)

    plt.show()
