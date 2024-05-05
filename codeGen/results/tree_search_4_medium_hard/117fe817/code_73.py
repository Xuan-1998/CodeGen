def findDigitOne(n):
    count = 0
    for i in range(1, n+1):
        count += int('1' * (i.bit_length() - i.bit_length() % 2) + str(i), 2).count('1')
    return count
