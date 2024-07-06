def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Function to build the tree and count good vertices
    def count_good_vertices(N, d):
        from collections import defaultdict, deque
        
        # Create adjacency list representation of the tree
        tree = defaultdict(list)
        idx = 1
        
        for i in range(N):
            for _ in range(d[i]):
                if idx < N:
                    tree[i + 1].append(idx + 1)
                    idx += 1
        
        # Function to determine good vertices using DFS
        def dfs(node):
            min_vertex = node
            for child in tree[node]:
                min_vertex = min(min_vertex, dfs(child))
            if min_vertex == node:
                good_vertices.append(node)
            return min_vertex
        
        good_vertices = []
        dfs(1)
        
        return len(good_vertices)
    
    result = count_good_vertices(N, d)
    print(result % MOD)

if __name__ == "__main__":
    main()

