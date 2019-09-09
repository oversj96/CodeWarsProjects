# Lucas Numbers

def lucas_numbers(n):
    numbers = [0, 1]
    i = 2
    while(len(numbers) < n):
        numbers.append(numbers[i-1] + numbers[i - 2])
        i += 1
    return numbers


print (lucas_numbers(20))

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 
# 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]