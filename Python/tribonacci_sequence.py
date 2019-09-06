def tribonacci(signature, n):
    for i in range(0, n-len(signature)):
        signature.append(signature[i] + signature[i+1] + signature[i+2])
    return signature[:n]

print(tribonacci([1, 1, 1], 10))