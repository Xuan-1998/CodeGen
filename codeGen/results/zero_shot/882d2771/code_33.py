import sys

t = int(input())
l, r = map(int, input().split())

# Initialize an array to store the values of f(n) for n from 2 to r-l+1
dp = [0] * (r - l + 3)
for i in range(2, r - l + 3):
    dp[i] = min(dp[i-1], dp[i-2]) + 1

result = 0
for i in range(t):
    result += i * pow(2, dp[r-l+1-i]) % (10**9 + 7)
print(result % (10**9 + 7))
