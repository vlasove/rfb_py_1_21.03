"""
Required Positional Args - необходимо-позициональные аргументы
"""

def add(a, b):
    """
    Арифметическое нечто
    """
    return a**2 + b**3 - 2*a*b*6

# Позициональность
print(add(2, 10))
print(add(10, 2))
print(add(b = 10, a = 2)) # Именованное обращение к параметрам

# Необходимость
print(add(1))
print(add(1, 2, 3))
