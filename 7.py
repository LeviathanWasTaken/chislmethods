import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (x - 1) * y / (x ** 2)

def analytical_solution(x):
    return np.exp(x - 1)

def euler_cauchy(x0, y0, h, xn):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn, n+1)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(n):
        y[i+1] = y[i] + h * f(x[i], y[i])

    return x, y

def runge_kutta(x0, y0, h, xn):
    n = int((xn - x0) / h)
    x = np.linspace(x0, xn, n+1)
    y = np.zeros(n+1)
    y[0] = y0

    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + k1/2)
        k3 = h * f(x[i] + h/2, y[i] + k2/2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return x, y

x_ec, y_ec = euler_cauchy(1, np.exp(1), 0.05, 2)

x_rk, y_rk = runge_kutta(1, np.exp(1), 0.05, 2)

x_analytical = np.linspace(1, 2, 100)
y_analytical = analytical_solution(x_analytical)

plt.plot(x_ec, y_ec, label='Euler-Cauchy')
plt.plot(x_rk, y_rk, label='Runge-Kutta 4th Order')
plt.plot(x_analytical, y_analytical, label='Analytical Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solutions of the Differential Equation')
plt.legend()
plt.grid(True)
plt.show()