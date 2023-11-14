from scipy.stats import binom

n = 100  # количество испытаний (выстрелов)
p = 0.8  # вероятность попадания в мишень

k = 85  # количество успехов (попаданий)

probability = binom.pmf(k, n, p)
print(f"Вероятность попадания ровно 85 раз из 100: {probability:.4f}")
