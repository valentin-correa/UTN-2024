def spaces(string):
    string_g = ""
    for i in range(len(string)):
        if string[i] != " ":
            string_g += string[i]
    return string_g

def combiner(string):
    str_good = ""
    i = 0
    while i < len(string):
        if i != len(string) - 5:
            str_good += string[i] + string[i+3]
            i += 1
        else:
            i += 3
            break
    while i < len(string):   
        str_good += string[i]
        i += 1
    
    return str_good

trys = int(input())
outputs = []

for i in range(trys):
    string = str(input())
    outputs.append(combiner(spaces(string)))
for i in range(len(outputs)):
    print(outputs[i])


