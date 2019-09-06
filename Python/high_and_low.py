def high_and_low(numbers):
    string_numbers = numbers.split()
    numbers = []
    for i in string_numbers:
        numbers.append(int(i))
    return str(max(numbers)) + " " + str

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))