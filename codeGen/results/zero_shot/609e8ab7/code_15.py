import sys

def min_operations(root, values):
    n = len(values)
    operations = 0
    
    # Process each vertex in order from leaf nodes to the root
    for i in range(n-1, -1, -1):
        adjustment = max(0, values[i] - l[i]) if values[i] < l[i] else min(0, r[i] - values[i])
        
        # Calculate the minimum number of operations needed for this vertex
        if adjustment > 0:
            operations += adjustment
        elif adjustment < 0:
            operations -= adjustment
        
    return operations

T = int(input())
for _ in range(T):
    n = int(input())
    parents = list(map(int, input().split()))
    values = []
    for _ in range(n):
        l, r = map(int, input().split())
        values.append((l, r))
    
    # Calculate the minimum number of operations needed
    root = 1
    while root < n:
        root = parents[root-1]
    min_ops = min_operations(root, [values[i][0] for i in range(n)])
    
    print(min_ops)
