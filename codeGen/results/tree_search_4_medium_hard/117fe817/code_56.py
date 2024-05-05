def findDigitOne(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        else:
            msb = (i // 10) % 10
            lsb = i % 10
            
            if msb == 0:
                dp[i] = dp[i - 1] + 1
            elif msb == 1:
                if lsb == 0:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1] + 2
            else:
                dp[i] = dp[i - 1] + lsb + 1
    
    return dp[n]

n = int(input())
print(findDigitOne(n))
