# Пример решения задачи M
sequence = input()
index = 0
counter = 0

for letter in sequence:
    if letter == "о":
        index += 1
        if index > counter:
            counter = index

    elif letter == "р":
        index = 0

print(counter)

# Однострочное решение
# print(len(max(input().split("р"))))