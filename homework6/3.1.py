import numpy as np
import scipy.stats as stats

# Рост дочерей
height_children = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
# Рост матерей
height_mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
# Вычисление разности средних значений
mean_diff = np.mean(height_children) - np.mean(height_mothers)
# Вычисление стандартного отклонения разности
std_diff = np.sqrt((np.var(height_children) / len(height_children)) + (np.var(height_mothers) / len(height_mothers)))
# Вычисление стандартной ошибки разности
standard_error_diff = std_diff * np.sqrt(1/len(height_children) + 1/len(height_mothers))
# Вычисление Z-значения для указанной доверительной вероятности
Z = stats.norm.ppf(0.975)  # Для уровня доверия 0.95 (двусторонний тест)
# Вычисление доверительного интервала для разности средних
lower_bound = mean_diff - Z * standard_error_diff
upper_bound = mean_diff + Z * standard_error_diff
# Вывод доверительного интервала для разности средних
print(f"95% Доверительный интервал для разности средних роста родителей и детей: ({lower_bound:.2f}, {upper_bound:.2f})")
