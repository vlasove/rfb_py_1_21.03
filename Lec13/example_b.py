# Блок определения/инициаилизации функции
def hello(): # <- сигнатура функции
    print("Greetings!") # <- тело функции

# Вызов явной функции!
hello()
hello()


# Что такое функция с точки зрения интерпретатора? Это объект
print(type(hello)) # type(hello)
print(hello) # hello и hello()
