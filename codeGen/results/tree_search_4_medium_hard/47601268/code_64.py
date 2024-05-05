dp = [1] * (n + 1)
for i in range(1, n + 1):
    hasConsecutiveOnes = False
    j = i - 1
    while j >= 0 and not hasConsecutiveOnes:
        if dp[j] > 0:
            hasConsecutiveOnes = bin(j).count('1') % 2 == 1
        j -= 1
    if not hasConsecutiveOnes:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = 0

print(dp[n])
