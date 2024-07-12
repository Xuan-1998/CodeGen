python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    adjacency_list = [[] for _ in range(N)]
    
    # Create the adjacency list based on the out-degrees
    current_vertex = 1
    for i in range(N):
        for _ in range(d[i]):
            adjacency_list[i].append(current_vertex)
            current_vertex += 1
    
    # DP array where dp[v][k] is the number of ways to form a subtree rooted at vertex v with exactly k good vertices
    dp = [[0] * (N + 1) for _ in range(N)]
    
    # Function to perform DFS and fill dp table
    def dfs(v):
        dp[v][1] = 1  # The subtree rooted at v itself with v being a good vertex
        total_good_vertices = 1
        
        for child in adjacency_list[v]:
            dfs(child)
            new_dp = [0] * (N + 1)
            
            for i in range(total_good_vertices + 1):
                if dp[v][i] == 0:
                    continue
                for j in range(1, N + 1):
                    if dp[child][j] == 0:
                        continue
                    new_dp[i + j] = (new_dp[i + j] + dp[v][i] * dp[child][j]) % MOD
            
            total_good_vertices += N
            for i in range(total_good_vertices + 1):
                dp[v][i] = new_dp[i]
    
    # Start DFS from the root (vertex 0)
    dfs(0)
    
    # Sum the number of good vertices for all trees
    result = sum(dp[0]) % MOD
    print(result)


