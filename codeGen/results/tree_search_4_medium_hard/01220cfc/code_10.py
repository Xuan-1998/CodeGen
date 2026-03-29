from sys import stdin

n = int(stdin.readline())
jumps = list(map(int, stdin.readline().split()))

dp = [False] * n
dp[0] = True  # base case: we can always reach the first element

for i in range(1, n):
    for j in range(i):
        if jumps[j] >= i - j and dp[j]:
            dp[i] = True
            break

print(dp[-1])  # print the final answer
