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


def make_level_lines_plot(f, f_grad, start, method, x_min, x_max, y_min, y_max, x_step=0.1, y_step=0.1, levels=None):
    trace = gradient_descent(f, f_grad, start, method, eps=1e-8)
    print(f'result: {trace[-1]}', f'iterations: {len(trace)}')
    if levels is None:
        levels = [f(args) for args in trace]
        list.sort(levels)
    x_s = np.arange(x_min, x_max, x_step)
    y_s = np.arange(y_min, y_max, y_step)
    z_s = np.array([[f(np.array([x, y])) for x in x_s] for y in y_s])

    plt.figure()
    cs = plt.contour(x_s, y_s, z_s, levels=levels)
    plt.clabel(cs)
    for i in range(len(trace) - 1):
        cur_point = trace[i]
        next_point = trace[i + 1]
        plt.scatter([cur_point[0]], [cur_point[1]])
        plt.plot([cur_point[0], next_point[0]], [cur_point[1], next_point[1]])
    plt.grid()
    plt.show()
