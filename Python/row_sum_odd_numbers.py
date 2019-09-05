# overthought way
def row_sum_odd_numbers(n):
    return sum(range(n**2 - n + 1, n**2 + n + 1, 2))

# simple way
def row_sum_odd_numbers2(n):
    return n**3

print(row_sum_odd_numbers(5))

# Pyramid Example
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...