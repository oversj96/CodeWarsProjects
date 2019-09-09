def dbl_linear(n):
    list = [1]
    list2 = []
    key = None
    start = 0
    for x in list:
        n1 = 2*x+1
        n2 = 3*x+1
        list.append(n1)
        list.append(n2)
        if(len(list) > n+1 == 0):
            list.sort()
            for x in range(start, len(list)):
                if(list[x] != key):
                    list2.append(x)
                key = list[x]
            start = x
    return list2[n-1]
        
print(dbl_linear(10))