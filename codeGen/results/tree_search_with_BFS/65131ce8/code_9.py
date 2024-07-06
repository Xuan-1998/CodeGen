python
MOD = 998244353

def count_good_vertices(N, d):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1  # Base case: single node tree
    
    # Iterate over the number of vertices
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                dp[i][j] = (dp[i][j] + dp[i - k][j - 1]) % MOD
    
    # Calculate the total number of good vertices
    total_good_vertices = 0
    for i in range(1, N + 1):
        total_good_vertices = (total_good_vertices + dp[N][i]) % MOD
    
    return total_good_vertices

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    result = count_good_vertices(N, d)
    print(result)

