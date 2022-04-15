"""
Variadic arguments - вариадические аргументы (вариационные, континуальные)
Континуальные аргументы - бывают 2-ух видов:
    1) Аргументы приводимые к кортежу
    2) Аргументы приводимые к словарю
"""

def print_info(**kwargs):
    """
    print_info:
        выводит информацию о переданных ему ИМЕНОВАННЫХ аругментах
    input:
        **kwargs - набор аргументов с именами (kwargs - KeyWord arguments)
    output:
        None
    """
    print(type(kwargs))
    print(kwargs)
    for k, v in kwargs.items():
        print("Key:",k, "Value:", v)

print_info(name="User", age=29, password="9189732uytgehwjk")
print_info()
