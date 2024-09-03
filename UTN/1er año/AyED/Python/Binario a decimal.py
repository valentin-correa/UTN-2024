def bin_dec(num_bin):
    ac = int()
    num_bin = num_bin[::-1]
    for i in range(len(num_bin)):
        ac += int(num_bin[i]) * 2 ** i
        
    return ac
num_bin = str(input())
print(bin_dec(num_bin))