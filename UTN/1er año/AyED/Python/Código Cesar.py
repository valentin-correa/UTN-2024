def nachei(string, strbom):
    string = str(input())
    jumps = int(input())
    for j in range(len(string)):
        index = 0
        index = abc.index(string[j])
        strbom += abc[abc.index(abc[index-jumps])]
    return strbom

trys = int(input())
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
strbom = ""
outputs = []

for i in range(trys):
    outputs.append(nachei(strbom))
for i in range(len(outputs)):
    print(outputs[i])
