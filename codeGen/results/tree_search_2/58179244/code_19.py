import sys

n = int(input())  # number of lamps
s = input()        # colors of the lamps (R, G, or B)

dp = [[False] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = True  # at most p recolors needed for any p

for p in range(1, n+1):
    for i in range(p, n+1):
        if s[i-1] == s[i-2]:  # adjacent lamps have the same color
            dp[i][p] = (dp[i-1][p-1] or dp[i-1][p]) and s[i-1] != s[i-2]
        else:
            dp[i][p] = True

for i in range(1, n+1):
    min_p = 0
    for p in range(n+1):
        if not dp[i][p]:
            min_p = max(min_p, p+1)
            break

print(min_p)  # minimum number of recolors needed to make the garland diverse

# construct a diverse garland with the minimum number of recolors
p = min_p
garland = []
for i in range(n):
    if dp[i][p-1] and s[i] == s[i+1]:
        p -= 1
    garland.append(s[i])

print(''.join(garland))  # diverse garland with the minimum number of recolors
