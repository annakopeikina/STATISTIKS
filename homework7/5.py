import numpy as np
from scipy.stats import t

# Данные
data = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
sample_mean = np.mean(data)
population_mean = 2.5  # Утверждаемое гипотетическое среднее
sample_std = np.std(data, ddof=1)  # Выборочное стандартное отклонение
n = len(data)  # Объем выборки

# Расчет t-статистики
t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(n))

# Рассчитываем критическое значение t для уровня значимости 5% и степеней свободы n-1
alpha = 0.05
degrees_of_freedom = n - 1
critical_value = t.ppf(1 - alpha, df=degrees_of_freedom)

print(f"t-статистика: {t_statistic:.4f}")
print(f"Критическое значение t: {critical_value:.4f}")

# Проверяем гипотезу
if np.abs(t_statistic) > critical_value:
    print("Отвергаем нулевую гипотезу: среднее отличается от утверждаемого значения.")
else:
    print("Принимаем нулевую гипотезу: нет оснований полагать, что среднее отличается от утверждаемого значения.")
