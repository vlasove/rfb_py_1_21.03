# Сравнение строк
lhs_word = "AAA"
rhs_word = "a"

print(lhs_word < rhs_word)

# ord(str) -> int, chr(int) -> str
# В Python все строки хранятся как unicode
# ASCII - сколько всего символов в стандарте
print("Code a is :", ord("a")) # 97
print("Code is A:", ord("A")) # 65
print("Code B is:", ord("B"))
print("Code Y is:", ord("Y"))

print("Character with 97 ordinal:", chr(97))
# for i in range(60, 150):
#     print(f"Character of {i}:", chr(i))


print("A" < "a")

print("abc" > "abcd")
# при сравнении двух строк (например, одинаковой длины)
# СНАЧАЛА СРАВНИВАЮТСЯ ПЕРВЫЕ СИМВОЛЫ!!!!!!! # "a" > "A" в случае, если
# можно сразу поставить знак > - возвращается True и дальнейшее сравнение не проводится!
# ЕСЛИ ПЕРВЫЕ СИМВОЛЫ РАВНЫ!!!! То выше указанные действия выполняется
# над ВТОРЫМИ СИМВОЛАМИ