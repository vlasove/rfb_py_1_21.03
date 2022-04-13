"""
Решение задачи H
"""

def multiply(a,b):
    """
    Арифметическое умножение аргументов
    """
    return a * b

def main():
    """
    Основная точка входа в приложение
    """
    first_arg, second_arg = int(input()), int(input())
    print(multiply(first_arg, second_arg))

main()