import numpy as np

def newton(f, f_g, f_h, x0, criterion, eps=1e-5, max_iters=1000):
    x = x0
    f_x = f(x)
    trace = [x]
    while True:
        f_g_x = f_g(x)
        f_h_x = f_h(x)
        f_h_inv = np.linalg.inv(f_h_x)
        delta = np.matmul(f_g_x, f_h_inv)
        x1 = x - delta
        f_x1 = f(x1)
        trace.append(x1)

        if  len(trace) == max_iters or \
            (criterion == 1 and np.linalg.norm(x1 - x) < eps) or \
            (criterion == 2 and abs(f_x1 - f_x) < eps) or \
            (criterion == 3 and np.linalg.norm(delta) < eps):
            return trace

        x = x1
        f_x = f_x1
