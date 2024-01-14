import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

zp_mean = np.mean(zp) # Вычисление средних значений
ks_mean = np.mean(ks)

covariance_manual = np.mean((zp - zp_mean) * (ks - ks_mean)) # Вычисление ковариации

zp_std_manual = np.sqrt(np.mean((zp - zp_mean)**2))  # Вычисление среднеквадратичных отклонений
ks_std_manual = np.sqrt(np.mean((ks - ks_mean)**2))
correlation_manual = covariance_manual / (zp_std_manual * ks_std_manual) # Вычисление коэффициента корреляции Пирсона

print(f"ковариация (ручной расчет): {covariance_manual:.4f}")
print(f"коэффициент корреляции Пирсона (ручной расчет): {correlation_manual:.4f}")
#_______________________________________________________________________________________________

zp2 = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks2 = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Найдем ковариацию с помощью np.cov
covariance_np = np.cov(zp2, ks2, ddof=0)[0][1]  # ddof=0 для выборки, ddof=1 для генеральной совокупности
# Найдем корреляцию Пирсона с помощью ковариации и среднеквадратичных отклонений
correlation_np = np.corrcoef(zp2, ks2)[0][1]
print(f"Ковариация (NumPy): {covariance_np:.4f}")
print(f"Корреляция Пирсона (NumPy): {correlation_np:.4f}")
