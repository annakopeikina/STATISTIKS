import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

data = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
confidence_level = 0.95

sample_mean = np.mean(data)
sample_std = np.std(data, ddof=1)  # Используем несмещенное стандартное отклонение (ddof=1)

# Рассчитываем значение t-статистики для уровня доверия 95% и степеней свободы (n-1)
t_value = t.ppf((1 + confidence_level) / 2, df=len(data) - 1)

# Вычисляем доверительный интервал
margin_of_error = t_value * (sample_std / np.sqrt(len(data)))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print(f"Нижняя граница доверительного интервала: {confidence_interval[0]:.4f}")
print(f"Верхняя граница доверительного интервала: {confidence_interval[1]:.4f}")
# Создаем scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(range(len(data)), data, label='IQ значения', color='blue')
plt.axhline(y=sample_mean, color='red', linestyle='--', label='Среднее значение')

# Отображаем доверительный интервал
plt.axhline(y=confidence_interval[0], color='green', linestyle='-', label='Доверительный интервал (95%)')
plt.axhline(y=confidence_interval[1], color='green', linestyle='-')

plt.xlabel('Номер наблюдения')
plt.ylabel('IQ значения')
plt.title('Scatter plot с доверительным интервалом')
plt.legend()
plt.grid(True)
plt.show()

