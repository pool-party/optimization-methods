import numpy as np

M = 1e9
EPSILON = 1e-12


def find_minimum(A, b, f):
    f = -np.array(f.copy()).astype(dtype=float)
    A = np.array(A.copy()).astype(dtype=float)
    b = np.array(b.copy()).astype(dtype=float)

    A = np.hstack((A, np.eye(len(b))))
    f = np.hstack((f, np.repeat(-M, len(b))))

    for i in range(len(b)):
        if b[i] < 0:
            A[i] = -A[i]
            b[i] = -b[i]

    for i in range(len(b)):
        f = f + A[i] * M

    col = np.argmax(f)
    basis = np.arange(len(A)) + len(A[0]) - len(b)

    while f[col] > EPSILON:

        row = -1
        min_b = np.inf

        for i in range(len(A)):
            if A[i, col] > EPSILON:
                b_res = b[i] / A[i, col]

                if b_res < min_b:
                    row = i
                    min_b = b_res

        if row == -1:
            print("Can't find resolve element")
            return

        resolve_el = A[row, col]
        basis[row] = col

        for i in range(len(A)):
            if i == row:
                continue
            else:
                if A[i, col] != 0:
                    k = A[i, col] / resolve_el
                    A[i] = A[i] - A[row] * k
                    b[i] = b[i] - b[row] * k

        k = f[col] / resolve_el
        f = f - A[row, :] * k
        A[row] = A[row] / resolve_el
        b[row] = b[row] / resolve_el

        col = np.argmax(f)

    result = [0 for _ in range(len(A[0]) - len(b))]
    for i in range(len(basis)):
        if basis[i] >= len(A[0]) - len(b):
            print("Dummy variable in the basis")
            return
        result[basis[i]] = b[i] / A[i, basis[i]]

    return result
