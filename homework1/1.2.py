import math

# Вычислим количество способов выбрать 3 кнопки из 10
combinations = math.comb(10, 3)

# Вероятность открыть дверь с первой попытки
probability = 1 / combinations

print("Вероятность открыть дверь с первой попытки:", round (probability, 5))
