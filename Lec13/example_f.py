"""
DOCSTRINGS - или строка-документации
Более-менее полезная функция
подсчет факториала n! = n * (n-1) * (n-2) * ... * 1
"""

def factorial(n):
    """
    функция подсчета факториала числа n
    n - натуральное число (>=0)
    возвращает целое положительное число : n!
    """
    res = 1
    if n <= 1:
        return res

    for i in range(2, n+1):
        res *= i 
    return res

for i in range(1, 11):
    res = factorial(i)
    print(f"{i}! is equal to {res}")