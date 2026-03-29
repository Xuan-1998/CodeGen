import sys

dp = [[[sys.maxsize for _ in range(len(s) + 1)] for _ in range(n + 1)] for _ in range(len(t) + 1)]

for i in range(1, len(t) + 1):
    for j in range(n + 1):
        jj = j
        for k in range(j * (len(s[jj]) + 1)):
            if k >= len(s[jj]):
                break
            if t[k:k + len(s[jj])] == s[jj]:
                dp[i][j][k] = min(dp[i-1][j][k - len(s[jj])], dp[i-1][jj][k]) + 1
                jj = j
        if dp[i][j][-1] != sys.maxsize:
            break

if any(row[-1] == sys.maxsize for row in dp[-1]):
    print(-1)
else:
    m = min(row[-1] for row in dp)
    used_strings = []
    pos = len(t) - 1
    while m > 0:
        for j in range(n, -1, -1):
            if dp[pos][j][-1] != sys.maxsize and dp[pos][j][-1] < m:
                used_strings.append((j, pos))
                m -= 1
                break
        pos -= 1
    print(m)
    for w, p in reversed(used_strings):
        print(f"{w} {p}")
