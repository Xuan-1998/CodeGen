def solve(n):
    dp = {0: 1}
    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        else:
            count = 0
            j = i - 1
            while j >= 0:
                if bin(j).count('1') > 1:
                    break
                count += 1
                j -= 1
            dp[i] = count + (dp.get(i-1, 0) or 0)
    return dp[n]

n = int(input())
print(solve(n))
