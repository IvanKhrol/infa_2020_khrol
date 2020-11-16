films = {}
print("Введите число первокурсников")
N = int(input())
for i in range(N):
    x = input()
    if films.get(x) != None:
        films[x] += 1
    else:
        films.setdefault(x, 1)
print(films)    