python
MOD = 998244353

def count_good_trees(N, d):
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[1][1] = 1  # Base case: root is a good vertex
    
    # Calculate number of ways to form subtrees
    for v in range(2, N + 1):
        for k in range(1, N + 1):
            if d[v - 1] == 0:
                dp[v][k] = dp[v - 1][k - 1]
            else:
                for u in range(1, v):
                    if d[u - 1] > 0:
                        dp[v][k] += dp[u][k - 1]
                        dp[v][k] %= MOD

    # Sum up the number of good vertices for all good trees
    result = 0
    for v in range(1, N + 1):
        for k in range(1, N + 1):
            result += dp[v][k]
            result %= MOD

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))

    # Ensure the input is valid
    assert len(d) == N
    assert sum(d) == N - 1
    assert d[0] >= 1

    result = count_good_trees(N, d)
    print(result)

