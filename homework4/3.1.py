import math

# Заданные параметры
mu = -2
sigma_squared = 32

# Вычисление математического ожидания (M(X))
mean = mu
print(f"Математическое ожидание M(X) = {mean}")

# Вычисление дисперсии (D(X))
variance = sigma_squared
print(f"Дисперсия D(X) = {variance}")

# Вычисление стандартного отклонения (std(X))
std_deviation = math.sqrt(variance)
print(f"Стандартное отклонение std(X) = {std_deviation : .4}")
