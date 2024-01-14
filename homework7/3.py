import numpy as np
import scipy.stats as stats

# Данные для первого и второго измерений
measurement_1 = [150, 160, 165, 145, 155]
measurement_2 = [140, 155, 150, 130, 135]
# Выполнение парного t-теста для зависимых выборок
statistic, p_value = stats.ttest_rel(measurement_1, measurement_2)
alpha = 0.05
print(f"Статистика t = {statistic:.2f}")
print(f"p-значение = {p_value:.4f}")
if p_value < alpha:
    print("Отвергаем нулевую гипотезу: существуют статистически значимые различия между первым и вторым измерениями.")
else:
    print("Нет оснований отвергнуть нулевую гипотезу: различия между первым и вторым измерениями статистически не значимы.")
