N = int(input())
L = []
for i in range(N):
    L.append(int(input()))
L.sort(reverse=True)
B = list(set(L))[2]
print(B, L.count(B))
