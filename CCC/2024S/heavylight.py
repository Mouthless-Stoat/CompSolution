def count_letter(input):
    out = {}
    for l in input:
        out[l] = 0 if l not in out else out[l] + 1
    return out


count = int(input().split(" ")[0])

for i in range(count):
    str = input()
    c = count_letter(str)
    last = ""
    last_state = 0

    for l in str:
        if last == l:
            
