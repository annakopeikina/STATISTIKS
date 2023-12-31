# Вероятность того, что все мячи белые
prob_all_white = (7/10) * (6/9) * (9/11) * (8/10)
print(f"Вероятность того, что все мячи белые: {prob_all_white:.3f}")

# Вероятность того, что ровно два мяча белые
prob_two_white = ((7/10) * (6/9) * (2/11) * (1/10)) + ((3/10) * (2/9) * (9/11) * (8/10))
print(f"Вероятность того, что ровно два мяча белые: {prob_two_white:.3f}")

# Вероятность того, что хотя бы один мяч белый
prob_at_least_one_white = 1 - ((3/10) * (2/9) * (2/11) * (1/10))
print(f"Вероятность того, что хотя бы один мяч белый: {prob_at_least_one_white:.3-f}")
