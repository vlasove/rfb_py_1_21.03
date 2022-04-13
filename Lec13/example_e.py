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

# Возврат нескольких значений
def calc(a, b):
    res1 = a ** 2 + b ** 2
    res2 = a ** 2 - b ** 2
    return (res1, res2)

value1, value2 = calc(2,4)
print("Value 1 :", value1)
print("Value 2 :", value2)