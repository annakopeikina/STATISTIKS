from math import comb

# Вычисление вероятности извлечения 3 белых мячей

# Вариант 1: 2 белых из первого ящика и 1 из второго
prob_2_white_from_box1 = (10 * 1) / 28 * (5 * 35) / 495

# Вариант 2: 1 белый из первого ящика и 2 из второго
prob_1_white_from_box1 = (5 * 3) / 28 * (10 * 21) / 495

# Вариант 3: 0 белых из первого ящика и 3 из второго
prob_0_white_from_box1 = (1 * 3) / 28 * (10 * 7) / 495

# Общая вероятность
probability = prob_2_white_from_box1 + prob_1_white_from_box1 + prob_0_white_from_box1

print(f"Общая вероятность: {probability:.4f}")




