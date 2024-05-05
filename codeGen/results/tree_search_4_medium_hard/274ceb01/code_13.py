from sys import stdin

n = int(stdin.readline())
marks = list(map(int, stdin.readline().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = min(dp[j-1] + marks[i-1] - sum(marks[k] for k in range(j)) for j in range(1, i+1))

print(min(dp))
