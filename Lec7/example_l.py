# Методы строк
msg = "######heLLo WorLLd 1W5316######"
# print(dir(msg)) # dir(obj)
# msg[0] = "!"
# NEW_MSG = "!"  + msg[1:]

# Измненение регистра строки
upper_msg = msg.upper()
print(".upper():", upper_msg)

lower_msg = msg.lower()
print(".lower():", lower_msg)

capitalize_msg = msg.capitalize()
print(".capitalize():", capitalize_msg)

# Узнать, на каком индексе стоит символ (первое вхождение)
if "W" in msg:
    print("index():", msg.index("W"))

# Узнать, сколько раз встрчечается та или иная подстрока
print(".count():", msg.count("LL"))

# .replace()
print(".replace():", msg.replace("#", "."))
#new_msg = msg.replace("#", ".").replace("!", ",").replace("?", "")

# strip()
print(".rstrip():", msg.rstrip("#"))
print(".lstrip():", msg.lstrip("#"))
print(".strip():", msg.strip("#"))