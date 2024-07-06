python
def solve():
    import sys
    input = sys.stdin.read
    MOD = 998244353
    
    data = input().split()
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    from collections import deque, defaultdict
    
    # Create the adjacency list for the tree
    adj = defaultdict(list)
    indegree = [0] * (N + 1)
    for i in range(1, N + 1):
        if d[i - 1] > 0:
            for j in range(d[i - 1]):
                adj[i].append(i + j + 1)
                indegree[i + j + 1] += 1
    
    # Topological sort to process nodes in a bottom-up manner
    topo_order = []
    queue = deque()
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # DP array to store the count of good vertices
    dp = [0] * (N + 1)
    
    # Process nodes in reverse topological order
    for node in reversed(topo_order):
        dp[node] = 1  # The node itself is a good vertex
        for neighbor in adj[node]:
            dp[node] += dp[neighbor]
            dp[node] %= MOD
    
    # The answer is the sum of dp values for all nodes
    result = sum(dp[1:]) % MOD
    
    print(result)


