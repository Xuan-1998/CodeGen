def min_operations(root, memo):
    if root in memo:
        return memo[root]

    children = [i for i in range(len(values)) if parents[i] == root]
    operations = float('inf')

    for child in children:
        operations = min(operations, values[child][1] - values[child][0] + min_operations(child, memo))
    
    memo[root] = operations
    return operations


T = int(input())
for _ in range(T):
    n = int(input())
    parents = list(map(int, input().split()))
    values = []
    for _ in range(n):
        l, r = map(int, input().split())
        values.append((l, r))

    memo = {i: float('inf') for i in range(1, n + 1)}
    print(min_operations(0, memo))
