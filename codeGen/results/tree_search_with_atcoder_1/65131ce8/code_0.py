python
MOD = 998244353

def count_good_trees(N, d):
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][0] = 1  # Base case: A single vertex with no children

    # Fill DP table
    for i in range(2, N + 1):
        for j in range(d[i-1] + 1):
            for k in range(1, i):
                if j >= d[k-1]:
                    dp[i][j] = (dp[i][j] + dp[i-k][j-d[k-1]]) % MOD

    # Count good vertices
    good_vertex_count = 0
    for i in range(1, N + 1):
        for j in range(d[i-1] + 1):
            if dp[N][j] > 0:
                good_vertex_count = (good_vertex_count + 1) % MOD

    return good_vertex_count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    result = count_good_trees(N, d)
    print(result)

