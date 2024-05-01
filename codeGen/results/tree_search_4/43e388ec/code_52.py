import sys

a, b = map(int, input().split())
dp = [0] * 31620

# Initialize the base case
dp[0] = (a ^ b) % (10**9 + 7)

for i in range(1, 31620):
    dp[i] = ((a ^ (b >> i)) + dp[i-1]) % (10**9 + 7)

print(sum(dp))
