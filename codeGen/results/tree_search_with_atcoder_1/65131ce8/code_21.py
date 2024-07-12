python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize the dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1  # Base case: one way to have a tree with one vertex and one good vertex
    
    # Fill the dp table
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            dp[i][j] = (dp[i-1][j-1] * d[i-1]) % MOD
            if i > j:
                dp[i][j] = (dp[i][j] + dp[i-1][j] * (i - j)) % MOD
    
    # Sum up the number of good vertices for all possible trees
    result = 0
    for i in range(1, N + 1):
        result = (result + dp[N][i] * i) % MOD
    
    print(result)

if __name__ == "__main__":
    solve()

