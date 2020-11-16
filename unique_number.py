A = list(map(int, input().split()))
B = list(map(int, input().split()))
AA = set()
BB = set()
for i in range(len(A)):
    AA.add(A[i])
print(len(AA))
for i in range(len(B)):
    BB.add(B[i])
print(len(BB))
print(len(AA | BB))