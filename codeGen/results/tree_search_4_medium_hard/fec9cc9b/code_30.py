dp = [[False]*n for _ in range(n)]
for i in range(1, n):
    increasing = True
    decreasing = True
    j = 0
    while j < i:
        if array[j] <= array[i]:
            decreasing = False
        else:
            increasing = False
        j += 1
    dp[i][0] = increasing and decreasing

for l, r in queries:
    print("Yes" if all(dp[r-i][l+1] for i in range(r-l)) else "No")
