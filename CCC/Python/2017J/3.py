p1 = map(eval, input().split())
p2 = map(eval, input().split())
bat = eval(input())
s = bat - sum(map(lambda x, y: abs(x - y), p1, p2))

print("Y" if s % 2 == 0 and s >= 0 else "N")
