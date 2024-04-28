def numPathsWithKCoins():
    K, N = map(int, input().split())
    arr = [[int(x) for x in input().split()] for _ in range(N)]

    dp = [[[False for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j][arr[i][j]] = True
            elif i > 0 or j > 0:
                total_coins = arr[i][j]
                for k in range(K+1):
                    if k <= total_coins:
                        dp[i][j][k] = (dp[i-1][j][k-arr[i][j]] or dp[i][j-1][k-arr[i][j]]) if k > 0 else True
                    else:
                        dp[i][j][k] = False

    return sum(sum([1 for x in row if x]) for row in dp[-1][-1])

print(numPathsWithKCoins())
