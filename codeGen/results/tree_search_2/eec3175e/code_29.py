code
n = int(input())
m = int(input())
nums = [int(x) for x in input().split()]

dp = [False] * (m + 1)
for num in nums:
    if num % m == 0:
        dp[num] = True
    for i in range(m - 1, -1, -1):
        if dp[i + num]:
            dp[i] = True

print(1 if dp[m] else 0)
