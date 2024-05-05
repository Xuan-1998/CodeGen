code = """
n = int(input())
for _ in range(n):
    t = input().strip()
dp = [[0] * (n + 1) for _ in range(len(t) + 1)]
s = []
for _ in range(n):
    s.append(input().strip())

for i in range(1, len(t) + 1):
    for j in range(1, n + 1):
        if t[i - 1] not in s[j - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + 1

m = dp[-1][-1]
print(m)

steps = []
i, j = len(t), n
while m > 0:
    if t[i - 1] in s[j - 1]:
        steps.append((j, i))
        i -= 1
        j -= 1
        m -= 1
    else:
        i -= 1
for step in steps:
    print(*step)
"""

