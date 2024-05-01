# Take input from stdin
a, b = map(int, input().split())
dp = [0] * (314160)

dp[0] = a ^ b

for i in range(1, 314160):
    dp[i] = (dp[i-1] ^ ((b >> i % 31) & 1)) % (10**9 + 7)

# Calculate the cumulative sum
ans = 0
for res in dp:
    ans += res

print(ans)
