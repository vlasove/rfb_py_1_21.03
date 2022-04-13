# Простейший возврат
def add(a, b):
    res = a**2 + b**2 - 3*a*b
    print("BEFORE PRINT")
    return res
    print('AFTER PRINT') # После передачи управления назад - последующий код становится недостижимым




result = add(11, 51) # в момент выполнения строки 6 происходит передача управления функции
                     # add. Она расчитывает некое значение, и передает управлдение
                     # назад с возвратом расчитанного значения
print(result)

def add_with_no_return(a, b):
    res = a**2 + b**2 - 3*a*b
    print("Result:", res)
    # return None
    # return

# Мораль- в Python  функции всегда возвращают что-то. Если разработчик ничего не указал - вернется None
print()
print()
result_with_no_return = add_with_no_return(10, 20)
print(result_with_no_return)