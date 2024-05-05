import sys

dp = [[False] * 2001 for _ in range(2001)]

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))

top = False

for i in range(n):
    for j in range(n):
        if i > j:
            i, j = j, i
        if (i == 0 or p[i-1] <= p[i]) and (j == 0 or p[j-1] >= p[j]):
            dp[i][j] = True
        else:
            for k in range(i, j+1):
                if not dp[i][k-1] and not dp[k+1][j]:
                    dp[i][j] = True
                    top = True

print("YES" if top else "NO")
