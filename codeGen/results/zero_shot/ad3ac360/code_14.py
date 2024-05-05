code
cuts = 0

for i in range(1, n):
    if not dp[i][i]:
        cuts += 1

print(cuts)
