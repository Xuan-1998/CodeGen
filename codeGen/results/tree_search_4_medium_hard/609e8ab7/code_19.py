def min_operations(root, ranges, memo):
    if root not in memo:
        memo[root] = 0
        for child in range(1, root+1):
            if child in ranges and child != root:
                l, r = ranges[child]
                min_ops = min(r-l+1, min_operations(child, [(l+x, r+x) for x in range(r-l+1)], memo))
                memo[root] += min_ops
    return memo[root]

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        ranges = [list(map(int, input().split())) for _ in range(n-1)]
        root_range = list(map(int, input().split()))
        
        # Convert tree structure to adjacency list
        graph = [[] for _ in range(n+1)]
        for i, (parent, left, right) in enumerate(ranges):
            graph[parent].append((i+1, (left, right)))
        
        memo = {}
        print(min_operations(1, [(0, 10**9)] + root_range, memo))

solve()
