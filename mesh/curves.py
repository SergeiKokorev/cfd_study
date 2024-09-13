from settings import *


def curve1(u):
    return u ** 2, u, u * 0


def grid(f, u, args=(), omega=0.1, eps=1e-6, max_iter=800):

    if max_iter == 0:
        raise RuntimeError('Solution not found. Maximum number of iterations exeeded')

    x = np.array(f(u, *args))
    unew = np.zeros(shape=(u.size, ))
    unew[0], unew[-1] = u[0], u[-1]

    for k in range(1, u.size - 1):
        w1 = np.linalg.norm(x[:, k] - x[:, k - 1])
        w2 = np.linalg.norm(x[:, k + 1] - x[:, k])
        utmp = (w1 * u[k - 1] + w2 * u[k + 1]) / (w1 + w2)
        unew[k] = (1 - omega) * u[k] + omega * utmp
    
    xnew = np.array(f(unew, *args))

    rms = np.linalg.norm(xnew - x)

    if rms <= eps:
        return xnew
    else:
        return grid(f, unew, args, omega, eps, max_iter - 1)


def comp_u(u0, u1, n):
    return np.array([u0 + i * (u1 - u0) / n for i in range(n+1)])


def simple_grid(f, u0, u1, n, args=()):

    du = (u1 - u0) / n
    u = np.array([u0 + i * du for i in range(n + 1)])
    return f(u)


if __name__ == "__main__":

    u0, u1, n = 0, 4, 8
    nodes_smooth = grid(curve1, comp_u(u0, u1, n))
    nodes_rough = simple_grid(curve1, u0, u1, n)

    fig, ax = plt.subplots()
    ax.plot(nodes_smooth[0], nodes_smooth[1], 'bo-', label='Smooth')
    ax.plot(nodes_rough[0], nodes_rough[1], 'ro', label='Normal')
    ax.grid(True)

    fig.legend()

    plt.show()