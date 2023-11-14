import math
# Задача перестановок
# Количество способов вытащить 4 крести из 13 крестей
ways_to_draw_4_kreuz = math.comb(13, 4)

# Количество способов вытащить 4 карты из 52
ways_to_draw_4_cards = math.comb(52, 4)

# Вероятность всех 4 крести
probability_all_kreuz = ways_to_draw_4_kreuz / ways_to_draw_4_cards

print("Вероятность что все крести ", round (probability_all_kreuz, 4))

# Всего карт в колоде
total_cards = 52

# Количество тузов в колоде
total_aces = 4

# Количество карт, которые нужно вытащить
cards_to_draw = 4

# Вероятность вытащить 4 карты без тузов
probability_no_ace = math.comb(total_aces, 0) * math.comb(total_cards - total_aces, cards_to_draw) / math.comb(total_cards, cards_to_draw)

# Вероятность хотя бы одного туза
probability_at_least_one_ace = 1 - probability_no_ace
# Округляем вероятность до двух знаков после запятой
probability_at_least_one_ace = round(probability_at_least_one_ace, 2)

print("Вероятность хотя бы одного туза:", probability_at_least_one_ace)
