import copy
import math

A = [[-0.13, -0.02, 0], [-0.02, 0, 0.1], [0, -0.1, 1]]
b = [0, 0.1, 1]
eps = 0.0001

def get_special_view(B: list, y: list) -> list:
    for i in range(len(B)):
        if B[i][i] == 0:
            B[i][i] = (0.99999 - sum(i for i in B[i])) / 2
            y[i] *= -1
        elif math.fabs(B[i][i]) >= 1:
            for j in B[i]:
                j *= 1/B[i][i]
            math.copysign(y[i], B[i][i])
            B[i][i] = 0
        else:
            B[i][i] += 1
            y[i] *= -1


def get_square_matrix_norm(B: list) -> float:
    s = 0
    m = -1000
    for i in range(len(B)):
        for j in range(len(B)):
            s += math.fabs(B[j][i])
        m = max(s, m)
        s = 0
    return m


def calculate_f(B: list, x: list, y: int) -> float:
    return sum(B[i]*x[i] for i in range(len(B))) - y


def get_solution(B: list, y: list):
    x_0 = [0] * len(B)
    x_1 = copy.deepcopy(x_0)
    k = 0
    while True:
        k += 1
        for i in range(len(x_1)):
            x_1[i] = calculate_f(B[i], x_0, y[i])
        if max(math.fabs(x_1[i] - x_0[i]) for i in range(len(x_1))) <= eps:
            print(k)
            return x_1
        x_0 = copy.deepcopy(x_1)


if __name__ == '__main__':
    B = copy.deepcopy(A)
    y = copy.deepcopy(b)
    get_special_view(B, y)
    print(*B, sep='\n')
    print(get_square_matrix_norm(B))
    x = get_solution(B, y)
    print(x)
    print(sum(x[i] * A[0][i] for i in range(3)))