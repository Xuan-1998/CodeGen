python
MOD = 998244353

def count_good_vertices(N, d):
    # Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1
    
    # Loop over number of vertices
    for i in range(2, N + 1):
        # Loop over possible number of good vertices
        for j in range(1, i + 1):
            # Calculate dp[i][j]
            for k in range(1, i):
                if d[k - 1] > 0:
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * d[k - 1]) % MOD
    
    # Sum the results for all possible number of good vertices
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    print(count_good_vertices(N, d))

