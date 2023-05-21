import math


def bisection_method(equation, a, b, accuracy):
    iterations = math.ceil(math.log2((b - a) / accuracy))
    for i in range(iterations):
        c = (a + b) / 2
        if equation(c) == 0 or (b - a) / 2 < accuracy:
            return c

        if equation(c) * equation(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


def equation(x):
    return math.cos(x + 0.3) - x ** 2


accuracy = 0.001
root = bisection_method(equation, -10, 0, accuracy)
print("Root:", root)

//pip install numpy matplotlib
