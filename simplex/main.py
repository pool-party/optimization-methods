from simplex import find_minimum
import numpy as np


def matrix(system, results, c):

    def less_or_equals(i, width):
        system[i][width] = 1

    def greater_or_equals(i, width):
        system[i] = [-x for x in system[i]]
        results[i] *= -1
        less_or_equals(i, width)

    width = len(system[0][0])
    length = len(results)

    system = [(row + [0 for _ in range(length)], compare) for row, compare in system]
    c += [0 for _ in range(length)]

    for i in range(len(system)):
        row, res = system[i]
        system[i] = row

        if res == '>=':
            greater_or_equals(i, width)
        elif res == '<=':
            less_or_equals(i, width)
        else:
            width -= 1

        width += 1

    return system, results, c

test_cases = [matrix(system, results, c) for system, results, c in
    [
        [
            [
                ([3, 1, -1, 1], '='),
                ([5, 1, 1, -1], '='),
                ([1, 0, 0, 0], '>='),
                ([0, 1, 0, 0], '>='),
                ([0, 0, 1, 0], '>='),
                ([0, 0, 0, 1], '>=')
            ],
            [4, 4, 0, 0, 0, 0],
            [-6, -1, -4, 5]
        ],
        [
            [
                ([1, -3, -1, -2], '='),
                ([1, -1, 1, 0], '='),
                ([1, 0, 0, 0], '>='),
                ([0, 1, 0, 0], '>='),
                ([0, 0, 1, 0], '>='),
                ([0, 0, 0, 1], '>=')
            ],
            [-4, 0, 0, 0, 0, 0],
            [-1, -2, -3, 1]
        ],
        [
            [
                ([1, 1, 0, 2, 1], '='),
                ([1, 1, 1, 3, 2], '='),
                ([0, 1, 1, 2, 1], '='),
                ([1, 0, 0, 0, 0], '>='),
                ([0, 1, 0, 0, 0], '>='),
                ([0, 0, 1, 0, 0], '>='),
                ([0, 0, 0, 1, 0], '>='),
                ([0, 0, 0, 0, 1], '>=')
            ],
            [5, 9, 6, 0, 0, 0, 0, 0],
            [-1, -2, -1, 3, -1]
        ],
        [
            [
                ([1, 1, 2, 0, 0], '='),
                ([0, -2, -2, 1, -1], '='),
                ([1, -1, 6, 1, 1], '='),
                ([1, 0, 0, 0, 0], '>='),
                ([0, 1, 0, 0, 0], '>='),
                ([0, 0, 1, 0, 0], '>='),
                ([0, 0, 0, 1, 0], '>='),
                ([0, 0, 0, 0, 1], '>=')
            ],
            [4, -6, 12, 0, 0, 0, 0, 0],
            [-1, -2, -1, 3, -1]
        ],
        [
            [
                ([1, 1, -1, -10], '='),
                ([1, 14, 10, -10], '='),
                ([1, 0, 0, 0], '>='),
                ([0, 1, 0, 0], '>='),
                ([0, 0, 1, 0], '>='),
                ([0, 0, 0, 1], '>=')
            ],
            [0, 11, 0, 0, 0, 0],
            [-1, 4, -3, 10]
        ],
        [
            [
                ([1, 3, 3, 1], '<='),
                ([2, 0, 3, -1], '<='),
                ([1, 0, 0, 0], '>='),
                ([0, 1, 0, 0], '>='),
                ([0, 0, 1, 0], '>='),
                ([0, 0, 0, 1], '>=')
            ],
            [3, 4, 0, 0, 0, 0],
            [-1, 5, 1, -1]
        ],
        [
            [
                ([3, 1, 1, 1, -2], '='),
                ([6, 1, 2, 3, -4], '='),
                ([10, 1, 3, 6, -7], '='),
                ([1, 0, 0, 0, 0], '>='),
                ([0, 1, 0, 0, 0], '>='),
                ([0, 0, 1, 0, 0], '>='),
                ([0, 0, 0, 1, 0], '>='),
                ([0, 0, 0, 0, 1], '>=')
            ],
            [10, 20, 30, 0, 0, 0, 0, 0],
            [-1, -1, 1, -1, 2]
        ]
    ]
]

if __name__ == '__main__':
    for matrix, results, c in test_cases:
        matrix = np.array(matrix)
        results = np.array(results)
        print(find_minimum(matrix, results, c))
