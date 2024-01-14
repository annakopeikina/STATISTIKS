import numpy as np

# Рост дочерей и матерей
height_children = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
height_mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

# Вычисление выборочных дисперсий
var_children = np.var(height_children, ddof=1)
var_mothers = np.var(height_mothers, ddof=1)
# Вычисление выборочных средних
mean_children = np.mean(height_children)
mean_mothers = np.mean(height_mothers)
# Разность средних
mean_difference = mean_children - mean_mothers
print(f"Разность средних: {mean_difference: .2f}")
print(f"Выборочная дисперсия для роста дочерей: {var_children:.2f}")
print(f"Выборочная дисперсия для роста матерей: {var_mothers:.2f}")
