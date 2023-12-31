import numpy as np
from scipy.stats import t
def search_D(arr):
    mean_arr = arr.mean()
    D = 0
    for i in arr:
        D += (mean_arr - i) ** 2
    D /= len(arr) - 1
    return D
# Рост матерей и дочерей
x = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169, 165])  # Рост матерей
y = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])  # Рост взрослых дочерей
# Вычисление t-статистики
D_x = search_D(x)
D_y = search_D(y)
D = (D_x + D_y) / 2
t_statistic = (x.mean() - y.mean()) / ((2 * D / len(y)) ** 0.5)
# Уровень значимости
alpha = 0.05  # Уровень значимости
# Степени свободы для t-распределения
df = len(y) - 1
# критическое значение t
t_critical = t.ppf(1 - alpha / 2, df)  # Для двустороннего теста (alpha/2 с каждой стороны)
if abs(t_statistic) > t_critical:
    print("Отвергаем нулевую гипотезу: есть статистически значимые различия в росте дочерей")
else:
    print("Принимаем нулевую гипотезу: нет статистически значимых различий в росте дочерей")

