import numpy as np
import scipy.stats as stats
from scipy.stats import f_oneway

# Данные для каждой группы учеников
group_1 = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
group_2 = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
group_3 = [57, 67, 49, 48, 47, 55, 66, 51, 54]

# Выполнение однофакторного дисперсионного анализа 
statistic, p_value = f_oneway(group_1, group_2, group_3)
alpha = 0.05

print(f"Статистика F = {statistic:.2f}")
print(f"p-значение = {p_value:.4f}")

if p_value < alpha:
    print("Отвергаем нулевую гипотезу: существуют статистически значимые различия между группами.")
else:
    print("Нет оснований отвергнуть нулевую гипотезу: различия между группами статистически не значимы.")
