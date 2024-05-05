def findDigitOne(n: int):
    dp = [0]
    for i in range(1, n + 1):
        if i == 1:
            dp.append(1)
        else:
            last_digit = i % 10
            if last_digit == 1:
                dp.append(dp[-1] + 1 + (i // 10))
            elif last_digit > 1:
                dp.append(dp[-1] + i // 10)
            else:
                dp.append(dp[-1])
    return sum(dp)

n = int(input())
print(findDigitOne(n))
