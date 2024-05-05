def countOnes(n):
    dp = [0 for _ in range(len(str(n)))])
    if n == 0:
        return 0
    
    for i in range(1, len(str(n))):
        for j in range(i+1):
            if (j + 1) * 10**(i-1) <= n:
                dp[i] += 1
            else:
                break
                
    totalOnes = sum(dp[j] * (10**(len(str(n))-j-1)) for j in range(len(str(n))))
    return totalOnes

n = int(input())
print(countOnes(n))
