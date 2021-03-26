import numpy as np


def gradient_descent(f, f_grad, start_arg, method, max_iterations=100, eps=1e-5):
    cur_arg = start_arg
    trace = [cur_arg]
    for _ in range(max_iterations):
        cur_grad = f_grad(cur_arg)
        left_border = 0. + eps
        right_border = 10.
        cur_step, _, _ = method(lambda step: f(cur_arg - step * cur_grad), left_border, right_border, eps)
        next_arg = cur_arg - cur_step * cur_grad
        trace.append(next_arg)

        if np.linalg.norm(cur_grad) < eps:
            return trace  # answer is trace[-1]
        cur_arg = next_arg
