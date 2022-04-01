# Решение задачи F
n_films_in_service = int(input())
films_in_service = set()
m_films_to_request = int(input())

for _ in range(n_films_in_service): # Наполняем множество фильмов на сервисе
    films_in_service.add(input())

for _ in range(m_films_to_request): # Проверяем, есть ли запрпшиваемые фильмы на сервисе
    film_to_request  = input()
    if film_to_request in films_in_service:
        print("ЕСТЬ")
    else:
        print("НЕТ В НАЛИЧИИ")