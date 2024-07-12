MOD = 998244353

def count_good_vertices(N, d):
    # dp[i][j] will store the number of ways to form a subtree with i vertices and j good vertices
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: one way to form an empty subtree with zero vertices and zero good vertices
    
    for i in range(1, N + 1):
        for j in range(N, -1, -1):
            for k in range(d[i - 1] + 1):
                if j >= k:
                    dp[j][i] = (dp[j][i] + dp[j - k][i - 1]) % MOD
    
    # The final answer is the sum of dp[N][j] for all j from 1 to N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    print(count_good_vertices(N, d))

