import math
import random

from matplotlib import pyplot as plt

scope = [2, 3]
a = 0.5


#Находим значение функции y для посроения графика
def calculate_equalation(x):
    return 2*x + (x/(1 + math.pow(x, 2))) - math.atan(x) - 4


#Вычисление приближения
def method_of_approximation(x):
    return 2 - (x / (2 * (1 + math.pow(x, 2)))) + math.atan(x) / 2


#Отображаем график
def print_graphic():
    range_x = 100
    x = [i for i in range(-range_x, range_x)]
    y = [calculate_equalation(i) for i in x]
    plt.plot(x, y)
    plt.plot([-range_x, range_x], [0, 0], color='g')
    plt.plot([0, 0], [min(y), max(y)], color='g')
    plt.show()


def find_solution():
    x_0 = random.choice(scope)
    eps = 0.0001
    k = 0
    while True:
        k += 1
        x_1 = method_of_approximation(x_0)
        if k == 1:
            print('Априорная оценка количества операций: ', int(math.log(eps * (1 - a) / math.fabs(x_1 - x_0), a)),
                  '\nНачальное приближение: ', x_0, '\nРезультат первой итерации: ', x_1)
        if math.fabs(x_1 - x_0) < eps:
            break
        x_0 = x_1
    print('Корень уравнения: {0}\nЗатраченое количество итераций: {1}'.format(x_1, k), sep='\n')


find_solution()
print_graphic()
