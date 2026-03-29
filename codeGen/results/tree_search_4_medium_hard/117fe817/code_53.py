def findDigitOne(n):
    dp = [0]
    for i in range(1, n+1):
        if i % 10 == 1:
            dp.append(dp[-1] + 1)
        else:
            dp.append(dp[-1])
    
    return sum(dp)

if __name__ == "__main__":
    n = int(input())
    print(findDigitOne(n))
