MOD = 998244353

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # We need to construct the tree based on the out-degrees
    from collections import defaultdict, deque
    
    # Initialize a list to store the children of each vertex
    children = [[] for _ in range(N + 1)]
    
    # We will use a queue to construct the tree
    queue = deque([1])
    current = 1
    
    for i in range(1, N):
        if not queue:
            break
        parent = queue.popleft()
        for _ in range(d[parent - 1]):
            current += 1
            if current > N:
                break
            children[parent].append(current)
            queue.append(current)
    
    # Dynamic Programming table to store the number of ways
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: dp[v][0] = 1 for all v
    for v in range(1, N + 1):
        dp[v][0] = 1
    
    # Function to perform DFS and fill the DP table
    def dfs(v):
        for u in children[v]:
            dfs(u)
            for k in range(N, -1, -1):
                dp[v][k] = dp[v][k] * dp[u][0] % MOD
                for j in range(1, k + 1):
                    dp[v][k] = (dp[v][k] + dp[v][k - j] * dp[u][j] % MOD) % MOD
    
    # Start DFS from the root
    dfs(1)
    
    # Sum the number of good vertices for all subtrees
    result = sum(dp[1][k] for k in range(1, N + 1)) % MOD
    
    # Output the result
    print(result)

if __name__ == "__main__":
    main()

