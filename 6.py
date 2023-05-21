import math

def f(x, N):
    return 1 / math.sqrt(x ** 2 + N)

def rectangle_rule(a, b, N, n):
    h = (b - a) / n
    integral_sum = 0

    for i in range(n):
        x = a + (i + 0.5) * h
        integral_sum += f(x, N)

    integral_sum *= h
    return integral_sum

def trapezoidal_rule(a, b, N, n):
    h = (b - a) / n
    integral_sum = (f(a, N) + f(b, N)) / 2

    for i in range(1, n):
        x = a + i * h
        integral_sum += f(x, N)

    integral_sum *= h
    return integral_sum

def simpsons_rule(a, b, N, n):
    h = (b - a) / n
    integral_sum = f(a, N) + f(b, N)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral_sum += 2 * f(x, N)
        else:
            integral_sum += 4 * f(x, N)

    integral_sum *= h / 3
    return integral_sum

def exact_integral(a, b, N):
    return math.log((math.sqrt(b ** 2 + N) + b) / (math.sqrt(a ** 2 + N) + a))

def calculate_errors(approximate_value, exact_value):
    deviation = abs(approximate_value - exact_value)
    relative_error = abs((exact_value - approximate_value) / exact_value) * 100
    return deviation, "{:.12f}".format(relative_error)

def main():
    a = 1.2
    b = 2.1
    N = 10
    n = 100

    rectangle_integral = rectangle_rule(a, b, N, n)
    trapezoidal_integral = trapezoidal_rule(a, b, N, n)
    simpsons_integral = simpsons_rule(a, b, N, n)
    exact_value = exact_integral(a, b, N)

    rectangle_deviation, rectangle_relative_error = calculate_errors(rectangle_integral, exact_value)
    trapezoidal_deviation, trapezoidal_relative_error = calculate_errors(trapezoidal_integral, exact_value)
    simpsons_deviation, simpsons_relative_error = calculate_errors(simpsons_integral, exact_value)

    print("Approximate Integral Values:")
    print("Rectangle Rule:", rectangle_integral)
    print("Trapezoidal Rule:", trapezoidal_integral)
    print("Simpson's Rule:", simpsons_integral)
    print("Exact Value:", exact_value)
    print("")

    print("Deviation from Exact Value:")
    print("Rectangle Rule:", rectangle_deviation)
    print("Trapezoidal Rule:", trapezoidal_deviation)
    print("Simpson's Rule:", simpsons_deviation)
    print("")

    print("Relative Error (%):")
    print("Rectangle Rule:", rectangle_relative_error)
    print("Trapezoidal Rule:", trapezoidal_relative_error)
    print("Simpson's Rule:", simpsons_relative_error)

if __name__ == "__main__":
    main()