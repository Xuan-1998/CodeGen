dp = [False] * (n + 2)
dp[0] = True

for i in range(1, n + 1):
    for j in range(i - 1, 0, -1):
        if dp[j]:
            if random.getrandbits(1):  # with probability 1/2
                dp[i] = not dp[i]
            break

print(dp[n])
