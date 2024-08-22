pal = str(input())
simbolo = str(input())
ac = 0

for i in range (len(pal)):
    if pal[i] == simbolo:
        ac += 1
print("Hay" , ac , "ocurrencias de" , simbolo)