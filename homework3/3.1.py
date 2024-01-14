# Заданные значения зарплат
salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Вычисление среднего арифметического
mean = sum(salaries) / len(salaries)

# Вычисление среднего квадратичного отклонения (стандартного отклонения)
squared_diff = sum((x - mean) ** 2 for x in salaries)
std_deviation = (squared_diff / len(salaries)) ** 0.5

# Вычисление смещенной и несмещенной оценок дисперсии
variance_biased = squared_diff / len(salaries)
variance_unbiased = squared_diff / (len(salaries) - 1)

# Вывод результатов с округлением до двух знаков после запятой
print(f"Среднее арифметическое: {round(mean, 2)}")
print(f"Среднее квадратичное отклонение: {round(std_deviation, 2)}")
print(f"Смещенная оценка дисперсии: {round(variance_biased, 2)}")
print(f"Несмещенная оценка дисперсии: {round(variance_unbiased, 2)}")

# Проверка
import statistics
salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150] # Заданные значения зарплат
mean = statistics.mean(salaries) # Вычисление среднего арифметического
std_deviation = statistics.stdev(salaries) # Вычисление среднего квадратичного отклонения (стандартного отклонения)
variance_biased = statistics.variance(salaries) # Вычисление смещенной и несмещенной оценок дисперсии
variance_unbiased = statistics.variance(salaries, xbar=mean)
print(f"Проверочное среднее арифметическое: {mean:.2f}")
print(f"Проверочное среднее квадратичное отклонение: {std_deviation:.2f}")
print(f"Проверочная смещенная оценка дисперсии: {variance_biased:.2f}")
print(f"Проверочная несмещенная оценка дисперсии: {variance_unbiased:.2f}")
