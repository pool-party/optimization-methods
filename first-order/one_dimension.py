from terminaltables import AsciiTable
from math import sqrt

"""
Contracts:
  - f is continuous
  - f is unimodal
"""


def fibonacci(n):
    global fibonaccis

    if n in fibonaccis:
        return fibonaccis[n]

    if n < 2:
        return 1

    result = fibonacci(n - 1) + fibonacci(n - 2)
    fibonaccis[n] = result
    return result


def dichtomy_method(f, ai, bi, epsilon, iterations=0, evaluations=0):
    print(f'dichotomy > [{ai}, {bi}]')
    if bi - ai < 2 * epsilon:
        return ai, iterations, evaluations

    # delta < epsilon / 2
    delta = epsilon / 2.5

    middle = (ai + bi) / 2
    x1 = middle - delta
    x2 = middle + delta

    if f(x1) > f(x2):
        return dichtomy_method(f, x1, bi, epsilon, iterations + 1, evaluations + 2)
    else:
        return dichtomy_method(f, ai, x2, epsilon, iterations + 1, evaluations + 2)


def golden_ratio_method(f, ai, bi, epsilon):
    def golden_ratio_method_helper(ai, bi, x1, fx1, iterations=0, evaluations=0):
        print(f'golden   > [{ai}, {bi}]')
        if bi - ai < 2 * epsilon:
            return ai, iterations, evaluations

        x2 = ai + bi - x1
        fx2 = f(x2)
        if x1 > x2:
            x1, x2 = x2, x1
            fx1, fx2 = fx2, fx1

        if fx1 > fx2:
            return golden_ratio_method_helper(x1, bi, x2, fx2, iterations + 1, evaluations + 1)
        else:
            return golden_ratio_method_helper(ai, x2, x1, fx1, iterations + 1, evaluations + 1)

    x1 = ai + (3 - sqrt(5)) * (bi - ai) / 2
    return golden_ratio_method_helper(ai, bi, x1, f(x1), 0, 1)


def fibonacci_method(f, ai, bi, epsilon):
    def fibonacci_method_helper(ai, bi, n, xprev, fprev, flag, iterations=0, evaluations=0):
        print(f'fibonacci> [{ai}, {bi}]')

        if bi - ai < epsilon or n == 1:
            return ai, iterations, evaluations

        if flag:
            x1 = xprev
            x2 = ai + fibonacci(n + 1) * (bi - ai) / fibonacci(n + 2)
            f1 = fprev
            f2 = f(x2)
        else:
            x1 = ai + fibonacci(n) * (bi - ai) / fibonacci(n + 2)
            x2 = xprev
            f1 = f(x1)
            f2 = fprev

        if f1 > f2:
            return fibonacci_method_helper(x1, bi, n - 1, x2, f2, True, iterations + 1, evaluations + 1)
        else:
            return fibonacci_method_helper(ai, x2, n - 1, x1, f1, False, iterations + 1, evaluations + 1)

    lower_bound = (bi - ai) / epsilon
    n = 2
    while fibonacci(n) < lower_bound:
        n += 1

    print(f'fibonacci> found n: {n}')

    xprev = ai + fibonacci(n) * (bi - ai) / fibonacci(n + 2)

    return fibonacci_method_helper(ai, bi, n, xprev, f(xprev), True, 0, 1)


def compare(f, a, b, epsilon):
    def get_results(name, method):
        (result, iterations, evaluations) = method(f, a, b, epsilon)
        return [name, f'{result:0.10f}', str(iterations), str(evaluations)]

    print(f'Computing f on [{a}, {b}] with epsilon = {epsilon}:\n')

    table = [
        ["method name", "result", "iterations", "evaluations"],
        get_results("dichtomy", dichtomy_method),
        get_results("golden ratio", golden_ratio_method),
        get_results("fibonacci", fibonacci_method)
    ]

    print("\n" + AsciiTable(table).table)


if __name__ == "__main__":
    fibonaccis = {}
    compare(lambda x: 100 * ((x - x ** 2) ** 2) + ((1. - x) ** 2), 0.6, 1.2, 1e-8)
    compare(lambda x: (x - 1) ** 2 + 10, -10000, 10000, 1e-8)
