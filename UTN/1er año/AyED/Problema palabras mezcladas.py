test = int(input())
for i in range(test):
    text_good = ""
    text = str(input())
    mitad = int(len(text) / 2) - 1

    for i in range(mitad, mitad - mitad * 2 - 2, -1):
        text_good += text[i]
    print(text_good)