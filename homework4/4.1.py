from scipy.stats import norm

# Заданные параметры
mean = 174  # среднее значение
std_dev = 8  # стандартное отклонение
# используется для вычисления кумулятивной функции распределения нормального распределения
#  (Cumulative Distribution Function - cdf).
# norm.cdf(x, mean, std_dev) принимает три параметра:
#x: значение случайной величины, для которой вы хотите вычислить вероятность;
#mean: среднее значение (математическое ожидание) нормального распределения;
#std_dev: стандартное отклонение нормального распределения. 
#Является симметричной

# а) больше 182 см
prob_a = 1 - norm.cdf(182, mean, std_dev)
print(f'a) Вероятность роста больше 182 см: {prob_a:.4f}')

# б) больше 190 см
prob_b = 1 - norm.cdf(190, mean, std_dev)
print(f'b) Вероятность роста больше 190 см: {prob_b:.4f}')

# в) от 166 см до 190 см
prob_c = norm.cdf(190, mean, std_dev) - norm.cdf(166, mean, std_dev)
print(f'c) Вероятность роста от 166 см до 190 см: {prob_c:.4f}')

# г) от 166 см до 182 см
prob_d = norm.cdf(182, mean, std_dev) - norm.cdf(166, mean, std_dev)
print(f'd) Вероятность роста от 166 см до 182 см: {prob_d:.4f}')

# д) от 158 см до 190 см
prob_e = norm.cdf(190, mean, std_dev) - norm.cdf(158, mean, std_dev)
print(f'e) Вероятность роста от 158 см до 190 см: {prob_e:.4f}')

# е) не выше 150 см или не ниже 190 см
prob_f = norm.cdf(150, mean, std_dev) + (1 - norm.cdf(190, mean, std_dev))
print(f'f) Вероятность роста не выше 150 см или не ниже 190 см: {prob_f:.4f}')

# ё) не выше 150 см или не ниже 198 см
prob_g = norm.cdf(150, mean, std_dev) + (1 - norm.cdf(198, mean, std_dev))
print(f'g) Вероятность роста не выше 150 см или не ниже 198 см: {prob_g:.4f}')

# ж) ниже 166 см
prob_h = norm.cdf(166, mean, std_dev)
print(f'h) Вероятность роста ниже 166 см: {prob_h:.4f}')
