import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
# Дано:
sample_mean = 174.2
population_variance = 25
sample_size = 27
confidence_level = 0.95

# Z-значение для уровня доверия 95%
z_value = norm.ppf((1 + confidence_level) / 2)

# Стандартная ошибка среднего
standard_error = np.sqrt(population_variance / sample_size)

# Границы доверительного интервала
margin_of_error = z_value * standard_error
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(f"Доверительный интервал для математического ожидания с надежностью 0.95: {confidence_interval}")

# Визуализация
# Генерация случайных данных с нормальным распределением для визуализации гистограммы
np.random.seed(0)
data = np.random.normal(loc=sample_mean, scale=np.sqrt(population_variance), size=1000)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black', label='Распределение роста футболистов')
plt.axvline(x=confidence_interval[0], color='red', linestyle='--', label='Доверительный интервал (95%)')
plt.axvline(x=confidence_interval[1], color='red', linestyle='--')
plt.xlabel('Рост футболистов')
plt.ylabel('Плотность вероятности')
plt.title('Гистограмма с доверительным интервалом для роста футболистов')
plt.legend()
plt.grid(True)
plt.show()