# Решение задачи M
n = int(input())

for i in range(-n, n + 1): # (-2, -1, 0, 1, 2)
    sq = i ** 2
    print(f"Квадрат числа {i} равен {sq}")