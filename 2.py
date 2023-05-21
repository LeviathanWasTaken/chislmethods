import math

def equation(x):
    return x**2 - 2*math.cos(x)

def simple_iteration_method(p0, accuracy):
    p = p0
    while True:
        p_next = math.sqrt(2*math.cos(p))
        if abs(p_next - p) < accuracy:
            return p_next
        p = p_next

def newton_method(p0, accuracy):
    p = p0
    while True:
        f = equation(p)
        f_prime = 2*p + 2*math.sin(p)
        p_next = p - f / f_prime
        if abs(p_next - p) < accuracy:
            return p_next
        p = p_next

p_simple_iteration = simple_iteration_method(1, 0.001)
print("Simple Iteration method:", p_simple_iteration)

p_newton = newton_method(1, 0.001)
print("Newton's method:", p_newton)