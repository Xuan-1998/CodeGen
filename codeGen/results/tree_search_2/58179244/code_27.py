from collections import deque

n = int(input())
colors = input()

dp = [[0, 0, 0] for _ in range(n + 1)]
dp[0][0] = dp[0][1] = dp[0][2] = 0

q = deque([(0, 0)])  # Initialize queue with (index, last color)
while q:
    i, prev_color = q.popleft()
    for j in range(3):
        if (j == 0 and prev_color != 'R') or \
           (j == 1 and prev_color != 'G') or \
           (j == 2 and prev_color != 'B'):
            dp[i][j] = min(dp[i][j], dp[i - 1][prev_color] + (1 if j != prev_color else 0))
    for j in range(3):
        q.append((i + 1, colors[j]))
r = 0
for i in range(3):
    r = max(r, dp[-1][i])
print(r)
print(''.join(['R' if i % 3 == 0 else 'G' if i % 3 == 1 else 'B' for i in range(n)]))
