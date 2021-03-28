from math import sqrt

"""
Contracts:
  - f is continuous
  - f is unimodal
"""

def log(verbose_flag, value):
    if verbose_flag:
        print(value)

def dichotomy_method(f, left, right, epsilon, verbose=False):

    iterations = 0
    evaluations = 0

    # delta < epsilon / 2
    delta = epsilon / 2.5

    while right - left >= 2 * epsilon:
        log(verbose, f'dichotomy > [{left}, {right}]')

        middle = (left + right) / 2
        x1 = middle - delta
        x2 = middle + delta

        if f(x1) > f(x2):
            log(verbose, (right - x1) / (right - left))
            left = x1
        else:
            log(verbose, (x2 - left) / (right - left))
            right = x2

        iterations += 1
        evaluations += 2

    return left, iterations, evaluations

def golden_ratio_method(f, left, right, epsilon, verbose=False):

    GOLDEN_CONSTANT = (3 - sqrt(5)) / 2
    x1 = left + GOLDEN_CONSTANT * (right - left)
    x2 = right - GOLDEN_CONSTANT * (right - left)
    f1, f2 = f(x1), f(x2)

    iterations = 0
    evaluations = 1

    while right - left >= 2 * epsilon:
        log(verbose, f'golden ratio> [{left}, {right}]')

        x2 = left + right - x1
        f2 = f(x2)
        if x1 > x2:
            x1, x2 = x2, x1
            f1, f2 = f2, f1

        if f1 > f2:
            log(verbose, (right - x1) / (right - left))
            left = x1
            x1, f1 = x2, f2
            x2 = right - GOLDEN_CONSTANT * (right - left)
            f2 = f(x2)
        else:
            log(verbose, (x2 - left) / (right - left))
            right = x2
            x2, f2 = x1, f1
            x1 = left + GOLDEN_CONSTANT * (right - left)
            f1 = f(x1)

        iterations += 1
        evaluations += 1

    return left, iterations, evaluations


fibonaccis = {}


def fibonacci_method(f, left, right, epsilon, verbose=False):

    def fibonacci(n):
        global fibonaccis

        if n in fibonaccis:
            return fibonaccis[n]

        if n < 2:
            return 1

        result = fibonacci(n - 1) + fibonacci(n - 2)
        fibonaccis[n] = result
        return result

    lower_bound = (right - left) / epsilon
    n = 2
    while fibonacci(n) < lower_bound:
        n += 1

    log(verbose, f'found fibonacci[{n}] = {fibonacci(n)}')

    x1 = left + fibonacci(n) * (right - left) / fibonacci(n + 2)
    x2 = left + fibonacci(n + 1) * (right - left) / fibonacci(n + 2)
    f1, f2 = f(x1), f(x2)

    iterations = 0
    evaluations = 1

    while n > -2:
        log(verbose, f'fibonacci> [{left}, {right}]')

        if f1 > f2:
            log(verbose, (right - x1) / (right - left))
            left = x1
            x1, f1 = x2, f2
            x2 = left + (fibonacci(n + 1) / fibonacci(n + 2)) * (right - left)
            f2 = f(x2)
        else:
            log(verbose, (x2 - left) / (right - left))
            right = x2
            x2, f2 = x1, f1
            x1 = left + (fibonacci(n) / fibonacci(n + 2)) * (right - left)
            f1 = f(x1)

        n -= 1
        iterations += 1
        evaluations += 1

    return left, iterations, evaluations
