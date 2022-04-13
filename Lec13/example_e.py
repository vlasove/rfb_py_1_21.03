# Возврат с условным оператором
def choice(num):
    if num % 2 == 0:
        return "кратно двум"
    if num % 3 == 0:
        return "кратен трем"
    return "не знаю, что это"

print(choice(4))
print(choice(9))
print(choice(11))