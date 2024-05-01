a, b = map(int, input().split())
dp = [0] * ((a | b).bit_length() + 1)
for i in range((a | b).bit_length()):
    dp[i+1] = (dp[i] + (((a >> i) ^ (b >> i)) % (10**9 + 7))) % (10**9 + 7)
print(dp[-1])
