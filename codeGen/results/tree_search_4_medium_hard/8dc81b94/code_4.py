def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # Initialize base case
    if n == 0:
        return "YES"
    
    # Fill up the dynamic programming table
    for i in range(n):
        for j in range(i, n):
            if arr[j] > 0:
                dp[i][j] = "NO"
            else:
                if i > 0:
                    dp[i][j] = (dp[i-1][j] == "YES") or (arr[i] <= arr[j])
                else:
                    dp[i][j] = arr[j] == 0
                if j < n - 1:
                    dp[i][j] = dp[i][j] and ((dp[i][j-1] == "YES") or (arr[i] >= arr[j+1]))
    
    return "YES" if dp[0][n-1] else "NO"
