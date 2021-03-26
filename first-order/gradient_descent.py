import numpy as np


def gradient_descent(f, f_grad, start_arg, method, step=None, max_iterations=10000, eps=1e-5):
    cur_arg = start_arg
    trace = [cur_arg]
    for _ in range(max_iterations):
        #         cur_arg = float(ceil(cur_arg))
        cur_grad = f_grad(cur_arg)
        #         cur_grad = float(ceil(f_grad(cur_arg)))
        #         print(cur_arg, cur_grad)
        left_border = 1e-8
        # right_border = 10.
        right_border = find_right_border(lambda step: f(cur_arg - step * cur_grad))
        if step is None:
            cur_step, _, _ = method(lambda step: f(cur_arg - step * cur_grad), left_border, right_border, eps)
        else:
            cur_step = step
        #         print(cur_step)
        next_arg = cur_arg - cur_step * cur_grad
        trace.append(next_arg)

        # if np.linalg.norm(next_arg - cur_arg):
        # if abs(next_value - cur_value) < eps:
        if np.linalg.norm(cur_grad) < eps:
            return trace  # answer is trace[-1]
        cur_arg = next_arg
    return trace


def find_right_border(f, eps=1e-8):
    left = 0. + eps
    right = 0.01
    initial_value = f(left)
    step = 0.01

    while f(right) <= initial_value + eps:
        step *= 2
        right += step

    return right
