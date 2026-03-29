n, m = map(int, input().split())
array = list(map(int, input().split()))
direction = [True] * n

dp = [[False] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    direction[i-1] = array[i-1] >= array[i-2]

for l in range(m):
    r = list(map(int, input().split()))
    dp[l][r[0]] = True
    for j in range(r[0]+1, r[1]+1):
        if (direction[j-1] and j > 1) or (dp[l][j-1] and array[l] <= array[j]) or (dp[l][j-1] and direction[j-1]):
            dp[l][r[1]] = True
            break

print("Yes" if dp[0][m-1] else "No")
