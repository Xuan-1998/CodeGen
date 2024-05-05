def findDigitsOne(n):
    dp = [0]
    for i in range(1, n+1):
        if i & 1:  # Check if the most significant bit is 1
            dp.append(dp[-1] + 1)
        else:
            dp.append(dp[-1])
    return sum(dp)

n = int(input())
print(findDigitsOne(n))
