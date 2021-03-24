def line_search(f, left, delta=0.01, eps=1e-3, multiplier=2):
    """
    With given x0 (left) and f
    Look for the another argument x1 where f(x1) > f(x0) + eps
    """
    assert delta > 0
    assert multiplier > 1
    assert eps > 0

    initial_value = f(left)
    right = left + delta

    step = delta

    while f(right) <= initial_value + eps:
        step *= multiplier
        right += step

    return right


# TODO raw version
# step_chooser always equal to `linear_step_chooser(method)` for specified `method` for now
def gradient_descent(f, f_grad, start_arg, step_chooser, eps=1e-5):
    cur_arg = start_arg
    # cur_value = f(cur_arg)
    trace = [cur_arg]
    while True:
        cur_grad = f_grad(cur_arg)
        cur_step = step_chooser(f, cur_grad, cur_arg)
        next_arg = cur_arg - cur_step * cur_grad
        trace.append(next_arg)

        # TODO: more stop criterion if needed
        if numpy.linalg.norm(next_arg - cur_arg) < eps:
            return trace  # answer is trace[-1]
        cur_arg = next_arg


# TODO raw version
def linear_step_chooser(method):
    """
    :param method: 1-dim method, takes function, left border and right border
    :return: step for gradient descent
    """
    def result(f, grad, arg):
        def linear_optimization_problem(step):
            return f(arg - step * grad)

        left_border = 0.
        right_border = line_search(linear_optimization_problem, left_border)
        answer, _, _ = method(linear_optimization_problem, left_border, right_border)
        return answer

    return result
