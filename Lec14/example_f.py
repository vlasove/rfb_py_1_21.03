"""
Variadic arguments - вариадические аргументы (вариационные, континуальные)
Континуальные аргументы - бывают 2-ух видов:
    1) Аргументы приводимые к кортежу
"""

def add(*args): 
    """
    add:
        функция вариадическое аргумента, подсчитывающая сумму
        всех входных значений
    input:
        *args - набор целых чисел
    output:
        сумма всех переданных целых чисел
    """
    print("Current args:", args)
    summ = 0
    for elem in args:
        summ += elem
    return summ

def calculation(*args):
    """
    calculation:
        функция-калькулятор
    input:
        *args - набор целых чисел
    output:
        - если не было передано ничего - возвращает None
        - если передано 1 число - возвращает его же
        - если передано 2 числа - возвращает сумму
        - если передано 3 числа - возвращает разность 3 чисел
        - если передано 4 и больше - возвращает произведение всех чисел
    """
    args_len = len(args)
    if args_len == 0:
        return None
    elif args_len == 1:
        return args[0]
    elif args_len == 2:
        return args[0] + args[1]
    elif args_len == 3:
        return args[0] - args[1] - args[2]
    else:
        mult = 1
        for elem in args:
            mult *= elem
        return mult

print(add())
print(add(1,2))
print(add(1,2,1,2,2,2,2,2,2,2,22,2,2,2,2,2,2,2,2,2,22,2,2))
print(add(0,1,0))

print(calculation())
print(calculation(1))
print(calculation(2,3))
print(calculation(1,2,3))
print(calculation(1,2,3,4,5))