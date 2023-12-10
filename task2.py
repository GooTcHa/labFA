import copy
import math

A = [[0, -0.2/1.3, 0], [0.2, 0, -0.1], [0, 0.1, 0]]
b = [0, 1, 1]
eps = 0.0001


#Ищем квадратичную норму матрицы B
def get_square_matrix_norm(B: list) -> float:
    s = 0
    m = -1000
    for i in range(len(B)):
        for j in range(len(B)):
            s += math.fabs(B[j][i])
        m = max(s, m)
        s = 0
    return m


#Вычисляем приближение
def calculate_f(B: list, x: list, y: int) -> float:
    return sum(B[i]*x[i] for i in range(len(B))) + y


#Решаем систему уравнений
def get_solution(B: list, y: list):
    x_0 = [0] * len(B)
    x_1 = copy.deepcopy(x_0)
    k = 0
    while True:
        k += 1
        for i in range(len(x_1)):
            x_1[i] = calculate_f(B[i], x_0, y[i])
        if sum(math.fabs(x_1[i] - x_0[i]) for i in range(len(x_1))) <= eps:
            print(f'Последняя итерация: {k}, x_1 = {x_1}, x_0 = {x_0}')
            return x_1
        print(f'Итерация: {k}, x_1 = {x_1}, x_0 = {x_0}')
        x_0 = copy.deepcopy(x_1)


if __name__ == '__main__':
    C = copy.deepcopy(A)
    y = copy.deepcopy(b)
    print('Кубическая норма матрицы : ', get_square_matrix_norm(C), '\n')
    x = get_solution(C, y)