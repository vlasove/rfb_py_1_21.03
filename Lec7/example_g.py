# Срезы строк
message = "Hello#world!"

new_message = message[0] + message[1] + message[2] + message[3] + message[4]
print("Message:", new_message)

slice_message = message[0:5:1] # str[start:stop[:step]
print("Slice message:", slice_message)

a_slice = message[0:5] # По умолчанию step = 1
print(a_slice)

b_slice = message[:5] # По умолчанию start = 0, step=1
print(b_slice)

c_slice = message[5::2] # От 5 индекса до конца c шагом 2
print(c_slice)

# Только с другим шагом
b_slice = message[:8:2] # По умолчанию start = 0
# От начала до 8 индекса (не включая) с шагом в 2
print(b_slice)

c_slice = message[8::3] # От 8 индекса до конца -> [8:]
# От 8 индекса до конца с шагом в 3 -> [8::3]
print(c_slice)

# Срез/слайс любой коллекции - это объект того же типа, что и коллекция
print(message[:-1:1])

# Синтаксический сахар для срезов - разворот строки
print(message[::-1])

print("Message:", message)