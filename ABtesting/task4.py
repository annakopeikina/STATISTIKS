# Наша продуктовая команда в ecommerce магазине планирует запустить тест,
# направленный на ускорение загрузки сайта. Одна из основных метрик bounce rate в GA = 40%.
# Мы предполагаем, что при оптимизации сайта она изменится минимум на 20%.
# Средний трафик 4000 человек в день. Посчитайте сколько нам нужно дней держать эксперимент
# при alpha = 5% и beta = 20%, % от трафика 5 %

import scipy.stats as stats
import math

# Заданные параметры
p0 = 0.4  # начальная вероятность успеха (bounce rate в GA)
min_effect = 0.2  # минимально значимый эффект
alpha = 0.05  # уровень значимости
beta = 0.2  # мощность теста (1 - beta)
daily_traffic = 4000  # средний трафик в человеках в день
traffic_fraction = 0.05  # доля трафика для теста
minutes_in_day = 24 * 60  # количество минут в сутках

# Вычисление размера выборки
p1 = p0 * (1 - min_effect)  # вероятность успеха после изменения
sd = math.sqrt(p0 * (1 - p0))
z_alpha = stats.norm.ppf(1 - alpha/2) # (two-tailed test)
z_beta = stats.norm.ppf(1 - beta)

sample_size = ((z_alpha * sd / min_effect) ** 2) + ((z_beta * sd / min_effect) ** 2)
sample_size = round(sample_size)

# Вычисление времени эксперимента в минутах
experiment_minutes = int(sample_size / (daily_traffic * traffic_fraction) * minutes_in_day)

print(f"Размер выборки: {sample_size}")
print(f"Минут эксперимента: {experiment_minutes}")
