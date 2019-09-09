def gap(g, m, n):
    if(m % 2 == 0):
        m += 1
    for i in range(m, n+1, 2):
        for x in range(2, i+1):
            if(i % x == 0 and i is not x):
                break
            elif(i == x):
                for j in range(i, i+g+1):
                    for y in range(2, j+1):
                        if(j % y == 0 and j is not y):
                            break
                        elif(j == i+g):
                            return [i, j]
        
    return None

print (gap(4,100,110))