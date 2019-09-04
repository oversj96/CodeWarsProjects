# My solution without built in python functions for int to bin rep.
def add_binary(a,b):
    sum = a + b
    n = 0
    string = ""
    while (sum >= 2**n):
        n = n + 1
    for i in range(n-1, -1, -1):
        if(sum >= 2**i):
            sum = sum - 2**i
            string = string + '1'
        else:
            string = string + '0'
    return(string)

# Using built in python functions
def add_binary2(a,b):
    return bin(a+b)[2:]

add_binary(256, 0)