"""
Аннотирование - специфический синтаксический сахар языка, который позволяет указать
ЖЕЛАЕМЫЙ ТИП входных аргументов
"""

def add(a :int, b :int) -> int:
    """
    description
    """
    return a + b

def main() -> None:
    """
    description
    """
    print(add(1,2))
    print(add("one", "two"))
    print(add([1,2,3], [3,4,5]))
    # print(add(1, "one"))

main()