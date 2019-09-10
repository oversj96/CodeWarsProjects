def dbl_linear(n):
    list = [1]
    result = []
    i = 0
    num = list[i]
    n1 = 2*num+1
    n2 = 3*num+1
    list.append(n1)
    list.append(n2)
    return result[n-1]
        
print(dbl_linear(50))