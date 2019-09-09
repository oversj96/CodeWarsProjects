def dbl_linear(n):
    list = [1]
    for x in list:
        n1 = 2*x+1
        n2 = 3*x+1
        if(n1 not in list):
            list.append(n1)
        if(n2 not in list):
            list.append(n2)
        list.sort()
        if(len(list) > n and x == list[n]):
            break
    return list[n]

print(dbl_linear(10000000))
print('')