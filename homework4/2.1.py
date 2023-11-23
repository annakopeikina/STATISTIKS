import math

# Известные значения
a = 0.5  # Левая граница
variance = 0.2  # Дисперсия

# Находим правую границу
b = math.sqrt(12 * variance) + a
print(f"Правая граница величины B: {b: .4}")

# Находим среднее значение
mean = (a + b) / 2
print(f"Среднее значение величины B: {mean: .4}")