uni = []
uni = input().split()

can_tot = int(input()) 

for i in range(can_tot):
    fcar = []
    con = []
    con = input().split()
    for i in range(len(uni)):
        if uni[i] in con:
            fcar.append(1)
        else:
            fcar.append(0)
    print(fcar)