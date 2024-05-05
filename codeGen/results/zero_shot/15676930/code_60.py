from collections import deque, defaultdict
import heapq
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Calculate the total joy if hare i is fed first
total_joy = 0
for i in range(n):
    if i == 0:
        total_joy += c[i]
    elif i == n - 1:
        total_joy += a[i-1]
    else:
        total_joy += b[i]

# Calculate the maximum possible total joy using dynamic programming
dp = [0] * (n + 1)
for i in range(1, n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + a[(i-1)%n] if i % 2 == 0 else b[(i-1)%n] if i % 2 == 1 else c[(i-1)%n])

print(max(0, dp[-1]))
