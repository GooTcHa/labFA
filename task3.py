import copy

alpha = 1 / 200
a = -2
b = 2
step = 0.05
m = (b - a) / step


def get_function_sum(f, s) -> float:
    return sum(s ** i * f[2 - i] for i in range(3))


def simpson_method_solution(f):
    return step * (get_function_sum(f, a) + get_function_sum(f, b) +
                   2 * sum(get_function_sum(f, a + 2 * (i + 1) * step) for i in range(int(m / 2))) +
                   4 * sum(get_function_sum(f, a + (2 * i + 1) * step) for i in range(int(m / 2))))


def new_x(x_0):
    temp = [x_0[0], x_0[0] + x_0[1], x_0[1]]
    integral = simpson_method_solution(temp)
    integral *= alpha
    x_1 = [1 + integral * x_0[0], integral * x_0[0]]
    return x_1


def find_iter(n):
    x_1 = [0, 0]
    for i in range(n):
        x_1 = new_x(copy.deepcopy(x_1))
        print('Итерация: ', i + 1, f'x_{i + 1}(t) = ', x_1[0], 't + ', x_1[1])


find_iter(50)
