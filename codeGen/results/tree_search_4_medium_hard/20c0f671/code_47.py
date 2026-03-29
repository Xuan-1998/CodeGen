import sys

n, h_max = map(int, input().split())
book_thickness = [0] * n
for i in range(n):
    book_thickness[i], _ = map(int, input().split())

dp = [[sys.maxsize] * (h_max + 1) for _ in range(n)]
prev_h = 0

for i in range(1, n):
    for h in range(h_max + 1):
        if h < book_thickness[i]:
            dp[i][h] = dp[i-1][h]
        else:
            dp[i][h] = min(dp[i-1][max(0, h-book_thickness[i])], dp[i-1][h])
    prev_h = h

print(min(dp[-1]))
