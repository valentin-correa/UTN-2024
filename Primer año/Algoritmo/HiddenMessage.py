N=int(input())
for i in range(N):
    message=""
    mes=str(input())+" "
    for j in range(len(mes)):
        if mes[j-1]==" " and mes[j]!=" ":
            message=message+mes[j]
    print(message)

