def max_score(arr, k, z):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # base case: when j=0, the maximum score is 0
    for i in range(n + 1):
        dp[i][0] = 0
    
    # fill in the table using dynamic programming
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = 0
            else:
                transitions = [arr[i - 1], arr[max(0, i - z)]]
                dp[i][j] = max(dp[i - 1][j - 1] + transitions[0], dp[i - 1][j - 1] + transitions[1])
    
    return dp[n][k]

# read input from stdin
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr, k, z))
