def findDigitOne(n):
    res = 0
    for i in range(1, n + 1):
        str_i = str(i)
        digit_count = sum(1 for c in str_i if c == '1')
        res += digit_count
    return res

n = int(input())
print(findDigitOne(n))
