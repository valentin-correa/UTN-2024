str1=str(input())
str2=str(input())
ac=[int() for i in range(len(str1))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str2[j]==str1[i]:
            ac[i]+= 1
ac.sort()
print(ac[len(ac)-1])