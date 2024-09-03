def morse(num):
    a = ""
    morse = {"0":"-..-", "1":"..-.", "2":"..-", "3":".-", "4":".-..", "5":"-..", "6":"-.-.", "7":"...-", "8":"-.-", "9":"-."}
    for i in range(len(num)):
        a = morse[num[i]]
        print(a, end=" ")

    return ""
    
def natural(num):
    a = ""
    nat = {"-..-":"0", "..-.":"1", "..-":"2", ".-":"3", ".-..":"4", "-..":"5", "-.-.":"6", "...-":"7", "-.-":"8", "-.":"9"}
    for i in range(len(num)):
        a = nat[num[i]]
        print(a, end=" ")

    return ""
    
num = str(input())
print(natural(num))
