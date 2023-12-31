import scipy.stats as stats

# Известные данные
sigma = 16  # Стандартное отклонение генеральной совокупности
sample_mean = 80  # Выборочное среднее
n = 256  # Объем выборки
confidence_level = 0.95  # Уровень доверия
# Вычисление стандартной ошибки среднего
standard_error = sigma / (n ** 0.5)
# Вычисление Z-значения для указанного уровня доверия
# Для уровня доверия 0.95 используем 0.975, так как это двусторонний тест
# (по 0.025 с обеих сторон хвоста)
Z = stats.norm.ppf(0.975)
# Вычисление доверительного интервала
lower_bound = sample_mean - Z * standard_error
upper_bound = sample_mean + Z * standard_error
# Вывод доверительного интервала
print(f"Доверительный интервал: ({lower_bound:.2f}, {upper_bound:.2f})")
