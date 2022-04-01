# Итерирование по строкам
message = "Hello world!"

# По индексам
for i in range(len(message)):
    print("Id:", i, "Letter:", message[i])

# По элементам (for each)
for letter in message: # letter - произвольное имя переменной
    print("Letter:", letter)


slice_message = message[::2]
# По индексам в срезе
for j in range(len(slice_message)):
    print("Id:", j, "Letter:", slice_message[j])

# По всем элементам среза
for q in slice_message:
    print("Letter:", q)