pal_1 = str(input())
pal_2 = str(input())
aux = ""

if len(pal_1) == len(pal_2):
    for i in range(len(pal_1) - 1, -1, -1):
        aux += pal_1[i]
    if pal_2 == aux:
        print("Si")
    else:
        print("No")
else:
    print("No")