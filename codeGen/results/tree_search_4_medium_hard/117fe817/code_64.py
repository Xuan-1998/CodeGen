def findDigits(n):
    total = 0
    for i in range(1, n+1):
        count = 0
        for p in range(len(str(i))):
            if str(i)[p] == '1':
                count += (10 ** (len(str(i)) - p - 1)) * (i // (10 ** (len(str(i)) - p - 1))) + min((10 ** (len(str(i)) - p - 1)), n - i)
        total += count
    return total

n = int(input())
print(findDigits(n))
