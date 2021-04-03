import numpy as np


def newton(f, f_g, f_h, x0, criterion, eps=1e-5, max_iters=1000, ram_instead=False):
    x = x0
    f_x = f(x)
    trace = [x  if not ram_instead else psutil.virtual_memory().used / 1024 / 1024]
    while True:
        f_g_x = f_g(x)
        f_h_x = f_h(x)
        delta = np.matmul(f_g_x, np.linalg.inv(f_h_x))
        x1 = x - delta
        f_x1 = f(x1)
        trace.append(x1  if not ram_instead else psutil.virtual_memory().used / 1024 / 1024)

        if len(trace) == max_iters or \
                (criterion == 1 and np.linalg.norm(x1 - x) < eps) or \
                (criterion == 2 and abs(f_x1 - f_x) < eps) or \
                (criterion == 3 and np.linalg.norm(delta) < eps):
            return trace

        x = x1
        f_x = f_x1
