import numpy as np
import scipy.stats as stats
from scipy.stats import f_oneway

# Данные для каждой группы измерений
before = [150, 160, 165, 145, 155]
after_10mins = [140, 155, 150, 130, 135]
after_30mins = [130, 130, 120, 130, 125]
# Выполнение однофакторного дисперсионного анализа 
statistic, p_value = f_oneway(before, after_10mins, after_30mins)
alpha = 0.05
print(f"Статистика F = {statistic:.4f}")
print(f"p-значение = {p_value:.4f}")
if p_value < alpha:
    print("Отвергаем нулевую гипотезу: существуют статистически значимые различия между группами.")
else:
    print("Нет оснований отвергнуть нулевую гипотезу: различия между группами статистически не значимы.")
