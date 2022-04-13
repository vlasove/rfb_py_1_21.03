"""
Решение задачи I
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

def combination(n ,m):
    """
    Число сочетаний из n по m штук
    """
    return factorial(n) // (factorial(m) * factorial(n - m))

def main():
    """
    Основная точка входа в приложение
    """
    n, m = int(input()), int(input())
    print(combination(n, m))

main()