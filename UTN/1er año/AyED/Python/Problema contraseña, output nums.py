def spaces(password):
    string_g = ""
    for i in range(len(password)):
        if password[i] != " ":
            string_g += password[i]
    return string_g

trys = int(input())
for j in range(trys):
    password = spaces(str(input()))
    pass_encry = ""
    for i in range(12):
        if password[i] in "GQaku":
            pass_encry += "0"
        elif password[i] in "ISblv":
            pass_encry += "1"
        elif password[i] in "EOYcmw":
            pass_encry += "2"
        elif password[i] in "FPZdnx":
            pass_encry += "3"
        elif password[i] in "JTeoy":
            pass_encry += "4"
        elif password[i] in "DNXfpz":
            pass_encry += "5"
        elif password[i] in "AKUgq":
            pass_encry += "6"
        elif password[i] in "CMWhr":
            pass_encry += "7"
        elif password[i] in "BLVis":
            pass_encry += "8"
        elif password[i] in "HRjt":
            pass_encry += "9"
    print(pass_encry)