from math import exp, factorial

# Дано
n = 5000  # количество лампочек
p = 0.0004  # вероятность перегорания одной лампочки
distribution = n * p  # лямбда параметр распределения Пуассона

# Вероятность того, что ни одна лампочка не перегорит
prob_zero_burnout = (exp(-distribution) * distribution**0) / factorial(0)

# Вероятность того, что перегорят ровно две лампочки
prob_two_burnout = (exp(-distribution) * distribution**2) / factorial(2)

print(f"Вероятность, что ни одна лампочка не перегорит: {prob_zero_burnout:.6f}")
print(f"Вероятность, что перегорят ровно две лампочки: {prob_two_burnout:.6f}")
