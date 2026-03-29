MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    if sum(d) != N - 1 or d[0] < 1:
        print(0)
        return
    
    from collections import defaultdict, deque
    
    # Create adjacency list for the tree
    adj = defaultdict(list)
    for i in range(1, N):
        for j in range(d[i]):
            adj[i + 1].append(i + 1 + j)
    
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: a single vertex is a good subtree with 1 good vertex
    for i in range(1, N + 1):
        dp[i][1] = 1
    
    # Process vertices in reverse order (bottom-up DP)
    for v in range(N, 0, -1):
        if v in adj:
            for u in adj[v]:
                for k in range(N, 0, -1):
                    for j in range(1, k):
                        dp[v][k] = (dp[v][k] + dp[v][k - j] * dp[u][j]) % MOD
    
    # Sum up the number of good vertices
    result = 0
    for v in range(1, N + 1):
        for k in range(1, N + 1):
            result = (result + dp[v][k] * k) % MOD
    
    print(result)


