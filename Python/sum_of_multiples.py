def solution(number):
    num = 0
    for i in range(number-1, 0, -1):
        if(i % 5 == 0 or i % 3 == 0):
            num = num + i
    return num

print(solution(10))  