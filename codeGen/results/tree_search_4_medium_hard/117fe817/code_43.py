def findDigitOne(n):
    ones = [0]
    for i in range(1, n+1):
        if i < 10:
            ones.append(i)
        else:
            count = len([j for j in range(i-9, i) if str(j).count('1') > 0]) + (i - 1)
            ones.append(count)
    return sum(ones)

n = int(input())
print(findDigitOne(n))
