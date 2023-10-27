import math

# Вычислим количество способов извлечь 3 окрашенные детали из 9
combinations_painted = math.comb(9, 3)

# Вычислим общее количество способов извлечь 3 детали из 15
combinations_total = math.comb(15, 3)

# Вычислим вероятность
probability = combinations_painted / combinations_total

print("Вероятность извлечь 3 окрашенные детали составляет", round (probability, 5))
