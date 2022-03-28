# Старый алгоритм мин/макс
# Вам заранее известны возмодные пределы вводимых значений!
# Напишем программу, которая будет принимать на вход целые положительные числа
# из диапазона [1,...,1000]
# Необходимо найти максимальное и минимальное введенное занчения

MIN_VALUE = 1001
MAX_VALUE = -1

while True:
    numeric = int(input())
    if numeric <= 0:
        break

    if numeric < MIN_VALUE:
        MIN_VALUE = numeric

    if numeric > MAX_VALUE:
        MAX_VALUE = numeric


print("Минимум:", MIN_VALUE)
print("Максимум:", MAX_VALUE)