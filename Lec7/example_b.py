# Решение задачи H
AGREE, DISAGREE  = "СОГЛАСЕН", "НЕ СОГЛАСЕН"

message = input()
first_letter, last_letter = message[0], message[-1]


letters = first_letter + last_letter
words = set(["да", "Да", "ДА", "дА", "АД", "ад", "Ад", "аД"])

if letters in words:
    print(AGREE)
else:
    print(DISAGREE)