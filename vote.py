films = {}
print("Введите число первокурсников")
N = int(input())
for i in range(N):
    x = input()
    if films.get(x) != None:
        films[x] += 1
    else:
        films.setdefault(x, 1)
list_films = list(films.items())
list_films.sort(key = lambda i: i[1])
list_films.reverse()
for i in list_films:
    print(i[0], ':', i[1])    