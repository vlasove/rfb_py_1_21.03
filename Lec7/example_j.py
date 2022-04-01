# Пример решения задачи K
message = input()
answer = ""

for letter in message[::2]:
    answer += letter * 3

print(answer)

# print("".join([letter*3 for letter in input()[::2]]))