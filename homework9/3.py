# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

import numpy as np

# Дано:
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Градиентный спуск для коэффициентов a и b (с интерсептом)
learning_rate = 0.00001  # Скорость обучения
iterations = 1000000  # Количество итераций

a = 0  # Начальное значение коэффициента a
b = 0  # Начальное значение интерсепта

n = len(zp)
# Оператор "-=" обновляет переменную на значение, вычисленное справа от оператора минус равно,
# заменяя текущее значение на разницу между текущим значением и значением справа от оператора.
for _ in range(iterations):
    a_gradient = (-2/n) * np.sum(zp * (ks - (a * zp + b)))  # Градиент для коэффициента a
    b_gradient = (-2/n) * np.sum(ks - (a * zp + b))  # Градиент для интерсепта b
    a -= learning_rate * a_gradient  # Обновляем коэффициент a
    b -= learning_rate * b_gradient  # Обновляем интерсепт b

print(f"Коэффициенты линейной регрессии (с интерсептом): a = {a:.4f}, b = {b:.4f}")
# Значения первой и третьей задачи похожие:
# Коэффициент линейной регрессии (с интерсептом): (a = 2.6205, b = 444.1774) vs (a = 2.6410, b = 441.3956)