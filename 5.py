import numpy as np

xi = np.array([3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5])
yi = np.array([25, 28, 30, 32, 36, 39, 41, 44, 46, 47])

A = np.vstack([xi, np.ones(len(xi))]).T
k, b = np.linalg.lstsq(A, yi, rcond=None)[0]

A = np.vstack([xi**2, xi, np.ones(len(xi))]).T
a2, a1, a0 = np.linalg.lstsq(A, yi, rcond=None)[0]

def lagrange_polynomial(x, xi, yi):
    n = len(xi)
    result = 0
    for i in range(n):
        term = yi[i]
        for j in range(n):
            if i != j:
                term *= (x - xi[j]) / (xi[i] - xi[j])
                result += term
    return result

def divided_difference(xi, yi):
    n = len(xi)
    if n == 1:
        return yi[0]
    return (divided_difference(xi[1: ], yi[1:]) - divided_difference(xi[:-1], yi[:-1])) / (xi[-1] - xi[0])

def newton_polynomial(x, xi, yi):
    n = len(xi)
    result = 0
    for i in range(n):
        term = divided_difference(xi[:i+1], yi[:i+1])
        for j in range(i):
            term *= (x - xi[j])
            result += term
    return result

def simplify_lagrange_polynomial(xi, yi):
    n = len(xi)
    result = ''
    for i in range(n):
        term = str(yi[i])
        for j in range(n):
            if i != j:
                term += f" * (x - {xi[j]}) / ({xi[i]} - {xi[j]})"
                result += term
            if i != n-1:
                result += ' + '
    return result

def simplify_newton_polynomial(xi, yi):
    n = len(xi)
    result = str(yi[0])
    for i in range(1, n):
        term = str(divided_difference(xi[:i+1], yi[:i+1]))
        for j in range(i):
            term += f" * (x - {xi[j]})"
            result += ' + ' + term
    return result

print(f"Linear Regression: y = {k:.2f}x + {b:.2f}")
print(f"Quadratic Regression: y = {a2:.2f}x^2 + {a1:.2f}x + {a0:.2f}")
print("Lagrange Polynomial:")
print(simplify_lagrange_polynomial(xi, yi))
print("Newton Polynomial:")
print(simplify_newton_polynomial(xi, yi))