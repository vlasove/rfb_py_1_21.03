"""
А как смешивать континуальные параметры?
"""

def constructor(*args, **kwargs):
    """
    * сначала указываются континуальный параметр (кортежный)
    * затем указываются KeyWord аргументы
    constructor:
        что-то строит
    input:
        *args - набор строк
        **kwargs - набор именованных аргументов с информацией о пользователе
    output:
        Строка - содердащая всю необходимую информацию про пользователя и его ввод
    """
    
    
    hobby_part = "Хобби: "
    if len(args) > 0:
        hobby_part += ", ".join(list(args))

    info_part = ""
    if "name" in kwargs.keys():
        info_part += "Имя: " + kwargs["name"]
    
    if "age" in kwargs.keys():
        info_part += ", Возраст: " + str(kwargs["age"])

    if "is_student" in kwargs.keys():
        info_part += " , Студент"

    general_result = info_part + " . " + hobby_part
    return general_result



print(constructor(
    "Любит сфоткать еду в инстаграм", 
    "Любит лежать на диване",
    "Ходит в фитнес клуб",
    name = "Полина",
    age = 20,
    is_student = True
    ))