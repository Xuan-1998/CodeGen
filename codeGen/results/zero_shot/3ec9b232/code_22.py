def solve():
    n = int(input())
    m = list(map(int, input().split()))
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    count = [[0] * (n+1) for _ in range(n+1)]
    
    # Initialize the base case
    dp[1][m[0]] = 1
    
    # Fill up the dynamic programming table
    for i in range(2, n+1):
        for j in range(i, -1, -1):
            if m[j-1] <= j:
                count[i][j] += sum(dp[k][m[k]] for k in range(i) if k < i and dp[k][m[k]] > 0)
            dp[i][j] = sum(count[k][m[k]] for k in range(i) for k2 in range(n+1) if k2 <= j and count[k][k2] > 0)
    
    # Print the result
    print((dp[n][n] + 7) % (10**9 + 7))

if __name__ == "__main__":
    solve()
