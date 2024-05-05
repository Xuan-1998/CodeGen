def countOnes(n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        j = 0
        while 10**j <= i:
            dp[i] += (i - int(str(i)[:j+1]).rjust(len(str(i)))[:-j-1]) // 10**j * (dp[int(str(i)[:j+1]).lstrip('0') or 0]+1)
            j += 1
    
    return dp[n]

n = int(input())
print(countOnes(n))
