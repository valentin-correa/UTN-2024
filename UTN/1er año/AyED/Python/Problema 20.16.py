def spaces(string):
    string_g = ""
    for i in range(len(string)):
        if string[i] != " ":
            string_g += string[i]
    return string_g
