def tribonacci(signature, n):
    for i in range(0, n-len(signature)):
        signature.append(sum(signature[-3:]))
    return signature[:n]

print(tribonacci([1, 1, 1], 10))