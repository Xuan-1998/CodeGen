def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    # Create a table to store the minimum number of multiplications
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill the table using dynamic programming
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + p[i] * p[k+1] * p[j+1] + dp[k+1][j])
    
    # Backtrack to find the optimal parenthesization
    s = ''
    i, j = 0, n - 1
    while i < j:
        if dp[i+1][j] == dp[i][j]:
            s += '(' + str(i + 1) + ')*'
            i += 1
        elif dp[i][j-1] == dp[i][j]:
            s += '(*' + str(j) + ')'
            j -= 1
        else:
            k = min(range(i+1, j), key=lambda x: dp[i][x] + p[x]*p[x+1]*p[j])
            s += '(' + str(i+1) + '*' + str(k+1) + ')*' + str(j)
            i = k
    if dp[0][n-1] == float('inf'):
        print("NO SOLUTION EXISTS")
    else:
        print(s[:-1])

if __name__ == "__main__":
    solve()
