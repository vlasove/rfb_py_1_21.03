"""
Смешивание всех типов аргументов
"""

def demo(first_num, second_num, *args, is_default=True, **kwargs):
    """
    description
    """
    print("Required-positional:", first_num, second_num)
    print("*args:", args)
    print("Default value arg:", is_default)
    print("**kwargs:", kwargs)


demo(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, is_default=False, name="User", age=20)