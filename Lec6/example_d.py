# Операции над множествами (простейшие)

numeric_set = set([10, 20, 30, 40, 50, 60])
# .add() - добавление элемента
numeric_set.add(-200)

# .pop() - удаление случайного элемента, если множество пустое - ошибка
elem = numeric_set.pop() 
print("Deleted elem:", elem)

# .remove(elem) - удаляет elem из множества, если elem нет во множестве - ошибка
numeric_set.remove(50)
print("Current set:", numeric_set)

# Проверка вхождения элемента во множество
if 50 in numeric_set:
    print("50 in numeric_set")
else:
    print("50 not in numeric_set")

# Пример удаления 50 из множества
to_delete = 50
if to_delete in numeric_set:
    numeric_set.remove(to_delete)
