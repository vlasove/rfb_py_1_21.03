"""
Что может пойти не так с RP args?
"""

def add(a, b = 3, c = 4):
    print("a is:", a)
    print("b is:", b)
    print("c is:", c)
    return a + b + c


print(add(2))
print(add(1, 2))
print(add(1, b = 2)) # только b будет равен 2, остальные - по умолчанию
print(add(2, 3, 5))
print(add(b=10, c =15, a= 22))