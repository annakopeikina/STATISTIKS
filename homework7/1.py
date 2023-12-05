import numpy as np
import scipy.stats as stats
from scipy.stats import mannwhitneyu
# Данные для выборок
x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]
# Выполнение U-теста Манна-Уитни. Этот тест не требует нормального
#  распределения данных и подходит для маленьких выборок
statistic, p_value = mannwhitneyu(x1, y1, alternative='two-sided')
alpha = 0.05
print(f"тест Манна-Уитни = {statistic:.4f}")
print(f"p-значение = {p_value:.4f}")
if p_value < alpha:
    print("Отвергаем нулевую гипотезу: существуют статистически значимые различия между выборками.")
else:
    print("Нет оснований отвергнуть нулевую гипотезу: различия между выборками статистически не значимы.")
