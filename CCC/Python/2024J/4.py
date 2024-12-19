I = "forloops"
O = "fxrlxxps"
Is = set(I)
Os = set(O)
sus = Is ^ Os
if len(sus) == 2:
    print(sus.pop(), sus.pop())
