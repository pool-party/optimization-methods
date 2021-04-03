import numpy as np
from tqdm import tqdm
import psutil


def conjugate_gradients_method(f, f_grad, start_arg, method, pb=False, criterion=1, step=None, max_iterations=10000,
                               eps=1e-5, ram_instead=False):
    cur_arg = start_arg
    trace = [cur_arg if not ram_instead else psutil.virtual_memory().used / 1024 / 1024]
    grad_list = []
    prev_p = None
    beta = None
    not_first_launch = False
    for i in (tqdm(range(max_iterations)) if pb else range(max_iterations)):
        cur_grad = f_grad(cur_arg)
        if criterion == 3 and np.linalg.norm(cur_grad) < eps:
            return trace
        grad_list.append(cur_grad)
        p = -cur_grad
        if not_first_launch:
            beta = (grad_list[-1] * grad_list[-1]) / (grad_list[-2] * grad_list[-2])
        if i % len(cur_arg) == 0:
            beta = None
        if beta is not None:
            p += beta * prev_p
        cur_value = f(cur_arg)
        left_border = 1e-8
        # right_border = 10.
        right_border = find_right_border(lambda step: f(cur_arg - step * p))
        if step is None:
            cur_step, _, _ = method(lambda step: f(cur_arg - step * cur_grad), left_border, right_border, eps)
        else:
            cur_step = step
        next_arg = cur_arg + cur_step * p
        next_value = f(next_arg)
        trace.append(next_arg if not ram_instead else psutil.virtual_memory().used / 1024 / 1024)

        if criterion == 1 and np.linalg.norm(next_arg - cur_arg) < eps:
            return trace
        elif criterion == 2 and abs(next_value - cur_value) < eps:
            return trace
        cur_arg = next_arg
        prev_p = p
        not_first_launch = True
    return trace  # answer is trace[-1]


def find_right_border(f, eps=1e-8):
    left = 0. + eps
    right = 0.01
    initial_value = f(left)
    step = 0.01

    while f(right) <= initial_value + eps:
        step *= 2
        right += step

    return right
