def findDigitOnes(n):
    total = 0
    for i in range(10, n+1, 10):
        total += str(i).count('1')
    return total

n = int(input())
print(findDigitOnes(n))
