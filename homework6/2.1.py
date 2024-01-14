import numpy as np
import scipy.stats as stats

# Заданные данные
data = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
# Вычисление выборочного среднего и стандартного отклонения
sample_mean = np.mean(data)
sample_std = np.std(data, ddof=1)  # Используем ddof=1 для коррекции несмещенности
# Вычисление стандартной ошибки среднего
standard_error = sample_std / np.sqrt(len(data))
# Вычисление Z-значения для указанной доверительной вероятности
Z = stats.norm.ppf(0.975)  # Для уровня доверия 0.95 (двусторонний тест)
# Вычисление доверительного интервала
lower_bound = sample_mean - Z * standard_error
upper_bound = sample_mean + Z * standard_error
# Вывод доверительного интервала
print(f"Доверительный интервал: ({lower_bound:.2f}, {upper_bound:.2f})")
