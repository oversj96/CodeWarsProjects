def dbl_linear(n):
    list = [1]
    i = 0
    key = None
    checkpoint = 0
    checkpoint_val = n
    for x in list:
        list.append(2*x+1)
        list.append(3*x+1)
        if(i == checkpoint_val):
            if(checkpoint == 3):
                break
            else:
                checkpoint += 1
                checkpoint_val = len(list)
        i += 1
    list.sort()
    sorted_list = []
    for y in list:
        if(y != key):
            sorted_list.append(y)
        key = y
    return sorted_list[n]