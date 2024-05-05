def tree_adjustments():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        
        parents = list(map(int, input().split()))
        ranges = [list(map(int, input().split())) for _ in range(n)]
        
        # Build the tree structure
        tree = {i: parent - 1 for i, parent in enumerate(parents)}
        tree[0] = None
        
        # Determine the ancestors of each vertex
        ancestors = {i: [] for i in range(1, n)}
        current = 0
        for i in range(1, n):
            while parents[i] != current:
                ancestors[i].append(current)
                current = parents[current]
        
        # Calculate the adjustments needed for each vertex
        adjustments = [abs(ranges[i][0] - ranges[i][1]) // (i + 1) for i in range(n)]
        
        print(sum(adjustments))
