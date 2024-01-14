import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import f_oneway
# Дано:
# Рост спортсменов 
football_players = [173, 175, 180, 178, 177, 185, 183, 182]
hockey_players = [177, 179, 180, 188, 177, 172, 171, 184, 180]
weightlifters = [172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]
# print(len(football_players), len(hockey_players), len(weightlifters))
# Выполнение дисперсионного анализа
f_statistic, p_value = f_oneway(football_players, hockey_players, weightlifters)
print(f"F-статистика: {f_statistic:.4f}")
print(f"P-value: {p_value:.4f}")
# Значение F-статистики - 5.5001 указывает на различия среднего роста между тремя группами.
# Значение p-value = 0.0105 ниже уровня значимости 0.05, => различия между средними значениями
# роста в этих группах являются статистически значимыми.
# Можно отвергнуть нулевую гипотезу и сделать вывод о том,
# что средний рост в одной из этих групп действительно выше, чем в других.

# Список всех данных
data = [football_players, hockey_players, weightlifters]

# Названия групп
labels = ['Футболисты', 'Хоккеисты', 'Штангисты']

# Создание boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=labels)
plt.title('Распределение роста среди спортсменов')
plt.xlabel('Тип спорта')
plt.ylabel('Рост')
plt.grid(True)
plt.show()