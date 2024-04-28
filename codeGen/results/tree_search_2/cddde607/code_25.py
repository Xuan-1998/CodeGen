def numPaths(arr, N, K):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 and j == 0:
            if arr[0][0] == K:
                return 1
            else:
                return 0
        
        total_coins = arr[i][j]
        for x in range(i+1):
            for y in range(j+1):
                if (x, y) != (i, j) and total_coins - arr[x][y] == K:
                    if dp(x, y-1) > 0 or dp(x-1, y) > 0:
                        result = 1
                        break
            else:
                continue
            break
        else:
            return 0
        
        result = dp(i-1, j) + dp(i, j-1)
        memo[(i, j)] = result
        return result
    
    return dp(N-1, N-1)
