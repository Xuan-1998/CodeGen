import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    has_consecutive_ones = False
    for bit in bin(i)[2:]:  # skip '0b' prefix
        if has_consecutive_ones and bit == '1':
            break
        has_consecutive_ones = (has_consecutive_ones or bit == '1')
    dp[i] = i if not has_consecutive_ones else dp[i - 1]

print(dp[n])
