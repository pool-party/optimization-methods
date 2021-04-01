import numpy as np
from tqdm import tqdm
import psutil


def gradient_descent(f, f_grad, start_arg, method, pb=False, criterion=1, step=None, max_iterations=10000, eps=1e-5, ram_instead=False):
    cur_arg = start_arg
    trace = [cur_arg if not ram_instead else psutil.virtual_memory().used / 1024 / 1024]
    for _ in (tqdm(range(max_iterations)) if pb else range(max_iterations)):
        #         cur_arg = float(ceil(cur_arg))
        cur_grad = f_grad(cur_arg)
        cur_value = f(cur_arg)
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
        next_value = f(next_arg)
        trace.append(next_arg if not ram_instead else psutil.virtual_memory().used / 1024 / 1024)

        if criterion == 1 and np.linalg.norm(next_arg - cur_arg) < eps:
            return trace  # answer is trace[-1]
        elif criterion == 2 and abs(next_value - cur_value) < eps:
            return trace
        elif criterion == 3 and np.linalg.norm(cur_grad) < eps:
            return trace
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
