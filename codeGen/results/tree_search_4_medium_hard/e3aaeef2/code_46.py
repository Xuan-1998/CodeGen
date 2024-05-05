def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(11)]
        max_length = [0] * (m + 1)
        
        # Base case: no operations
        dp[1][0] = 1
        
        for i in range(2, 11):
            for j in range(m + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] * (i-1) + 1)
        
        # Calculate the maximum length for each number of operations
        for j in range(m + 1):
            if j == 0:
                max_length[j] = 0
            else:
                max_length[j] = max(max_length[j-1], dp[9][j] + 1)
        
        # Print the result modulo 10^9+7
        print((max_length[m] % (10**9 + 7)))

if __name__ == "__main__":
    solve()
