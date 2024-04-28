from collections import deque

n = int(input())
s = input()

dp = [[float('inf')] * 3 for _ in range(n + 1)]
dp[0] = [0, 0, 0]

for i in range(1, n + 1):
    c = ord(s[i - 1]) - ord('R'
    dp[i][c] = min(dp[i - 1][(c + 1) % 3] + (1 if s[i - 1] != 'R' else 0), 
                   dp[i - 1][(c + 2) % 3] + (1 if s[i - 1] != 'G' else 0))

r = dp[n][ord(s[0]) - ord('R')]
t = deque()
i, c = n, ord(s[0]) - ord('R')
while i > 0:
    t.appendleft((c, s[i - 1]))
    if c == (ord(s[i - 1]) - ord('R')):
        r -= 1
    c = ((c + 1) % 3)
    i -= 1

print(r)
for color, lamp in t:
    print(lamp, end='')
