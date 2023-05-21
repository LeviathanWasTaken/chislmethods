import numpy as np

def simple_iterations(A, b, epsilon):
    n = len(A)
    x = np.zeros(n)
    x_prev = np.zeros(n)
    iteration = 0

    while True:
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1: ], x_prev[i+1:])) / A[i, i]

        iteration += 1
        if np.linalg.norm(x - x_prev) < epsilon:
            break

        x_prev = np.copy(x)

    print("Simple Iterations:")
    print("Number of iterations:", iteration)
    print("Solution:", x)

def gauss_seidel(A, b, epsilon):
    n = len(A)
    x = np.zeros(n)
    iteration = 0

    while True:
        x_prev = np.copy(x)

        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1: ], x[i+1:])) / A[i, i]

        iteration += 1
        if np.linalg.norm(x - x_prev) < epsilon:
            break

    print("Gauss-Seidel:")
    print("Number of iterations:", iteration)
    print("Solution:", x)

A = np.array([[-7, 3, 2], [2, -5, 2], [1, 1, -4]])
b = np.array([-3, -2, 0])
epsilon = 0.0001

simple_iterations(A, b, epsilon)
gauss_seidel(A, b, epsilon)