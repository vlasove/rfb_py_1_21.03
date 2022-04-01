# Решение задачи C
n_cpp = int(input())
m_rust = int(input())

students = set()

for _ in range(n_cpp + m_rust):
    students.add(input()) # union

print(2*len(students) - m_rust - n_cpp)

