# Вероятность попадания каждым из стрелков
P_A1 = 0.9  # Вероятность попадания первым стрелком
P_A2 = 0.8  # Вероятность попадания вторым стрелком
P_A3 = 0.6  # Вероятность попадания третьим стрелком

# Вероятность выбора каждого из стрелков
P_B1 = 1 / 3  # Вероятность выбора первого стрелка
P_B2 = 1 / 3  # Вероятность выбора второго стрелка
P_B3 = 1 / 3  # Вероятность выбора третьего стрелка

# Вероятность поражения мишени (общая вероятность попадания любым стрелком)
P_A = P_A1 * P_B1 + P_A2 * P_B2 + P_A3 * P_B3

# Вычисление вероятности того, что выстрел произведен каждым из стрелков при условии попадания в мишень (по формуле Байеса)
P_B1_given_A = (P_A1 * P_B1) / P_A  # Вероятность того, что выстрел произведен первым стрелком при условии попадания
P_B2_given_A = (P_A2 * P_B2) / P_A  # Вероятность того, что выстрел произведен вторым стрелком при условии попадания
P_B3_given_A = (P_A3 * P_B3) / P_A  # Вероятность того, что выстрел произведен третьим стрелком при условии попадания

# Вывод результатов
print(f"Вероятность поражения мишени первым стрелком: {P_B1_given_A:.4f}")
print(f"Вероятность поражения мишени вторым стрелком: {P_B2_given_A:.4f}")
print(f"Вероятность поражения мишени третьим стрелком: {P_B3_given_A:.4f}")
