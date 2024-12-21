I = input()
O = input()

Is = set(I)
Os = set(O)

a = list(Is - Os)
b = list(Os - Is)[0]

if len(a) == 1:
    print(a[0], b)
    print("-")
else:
    a1, a2 = a

    if I.replace(a1, b).replace(a2, "") == O:
        print(a1, b)
        print(a2)
    else:
        print(a2, b)
        print(a1)
