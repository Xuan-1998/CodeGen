def max_score(arr):
    n = len(arr)
    k = int(input())
    z = min(5, k)

    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i+1, k)+1):
            if j == 0:
                dp[i][j] = arr[0]
            elif j < z or i == 0:
                dp[i][j] = max(dp[i-1][j-1] + arr[i], dp[i-1][j] + arr[i])
            else:
                dp[i][j] = max(dp[i-1][z-1] + arr[i], dp[i-1][z] + arr[i])

    return dp[-1][-1]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    print(max_score(list(map(int, input().split()))))
