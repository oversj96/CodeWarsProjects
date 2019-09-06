def find_outlier(integers):
    e = 0
    o = 0
    for i in range(0, 3):
        if (integers[i] % 2 == 0):
            e = e + 1
        else:
            o = o + 1
    if(e > o):
        for i in integers:
            if(i % 2 != 0):
                return i
    else:
        for i in integers:
            if(i % 2 == 0):
                return i


#print(find_outlier([2, 4, 6, 8, 10, 3]))
#print(find_outlier([-9224055, -4028738, 401615, -1929541, 9487969, 5473405, 4559883, 894579, -966465, 42525, 2258809, 1165203, 4675777, -9996253, -1650951, -8909849, -1465789, -4420729, 7126351, 5232665, -5282733, -2506905, -5591657, -122231, -9953633]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))