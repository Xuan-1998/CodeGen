def max_score(arr, k, z):
    n = len(arr)
    dp = [[-float('inf')] * (k+1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = arr[i]

    for j in range(1, k+1):
        for i in range(j, n):
            left_score = -float('inf') if i-j+z > 0 else dp[i-j+z][j-z] + arr[i]
            right_score = -float('inf') if i-j+2 <= n else dp[0][j-1] + arr[i+1]

            dp[i][j] = max(left_score, right_score)

    return dp[-1][-1]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr, k, z))
