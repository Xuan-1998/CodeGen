dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    count = 0
    for j in range(i):
        if bin(j).count('1') == len(bin(j)) - 2:  # Check if consecutive ones are present
            count += dp[j]
    dp[i] = count

print(dp[n])
