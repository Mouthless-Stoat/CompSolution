count = int(input())
hat_num = [input() for _ in range(count)]

count = 0
for i, n in enumerate(hat_num):
    if n == hat_num[int((i + (len(hat_num) / 2)) % len(hat_num))]:
        count += 1

print(count)
