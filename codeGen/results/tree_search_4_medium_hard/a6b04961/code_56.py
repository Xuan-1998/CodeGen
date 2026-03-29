import heapq

def max_hedgehog_bauty(n, m, edges):
    memo = {}
    
    def dfs(path, last_node):
        if (path, last_node) in memo:
            return memo[(path, last_node)]
        
        tail_beauty = len(path)
        spine_beauty = 0
        
        for edge in edges:
            u, v = edge
            if u == last_node:
                new_path = list(path)
                new_path.append(v)
                beauty = dfs(new_path, v)
                spine_beauty += beauty
            elif v == last_node:
                new_path = list(path)
                new_path.append(u)
                beauty = dfs(new_path, u)
                spine_beauty += beauty
        
        memo[(path, last_node)] = tail_beauty * (spine_beauty + 1)
        return tail_beauty * (spine_beauty + 1)
    
    max_bauty = 0
    for _ in range(m):
        heapq.heappop(edges)
        edge = heapq.heappop(edges)
        u, v = edge
        beauty = dfs([u], u)
        if beauty > max_bauty:
            max_bauty = beauty
    
    return max_bauty

# Input the number of nodes and edges.
n, m = map(int, input().split())

# Read in all the edges.
edges = [(map(int, input().split()),) for _ in range(m)]

print(max_hedgehog_bauty(n, m, edges))
