from collections import defaultdict

n = int(input())
colors = input()

dp = defaultdict(int)
last_color = None
min_rec = 0

for i in range(n):
    if i > 0:
        for c in set(colors[:i]):
            if last_color != c and c not in dp[i-1]:
                min_rec += 1
    last_color = colors[i]
print(min_rec)
