import heapq

def adjust_tree_values():
    n = int(input())
    parent = list(map(int, input().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, input().split())
        ranges.append((l, r))
    
    dp = [[float('inf')] * 100010 for _ in range(4)]
    dp[0][0] = 0
    
    def dfs(node, value, add_value):
        if node > n:
            return float('inf')
        
        l, r = ranges[node - 1]
        operations = abs(value - l) + abs(value - r)
        
        for i in range(4):
            dp[i][value] = min(dp[i][value], operations + (i == add_value))
        
        if parent[node]:
            left_ops = dfs(parent[node], value, not add_value)
            right_ops = dfs(n, value + 1 if add_value else -1, not add_value)
            return min(left_ops, right_ops) + 1
        else:
            return operations
    
    print(min(dfs(1, 0, False), key=lambda x: x[0]))

if __name__ == "__main__":
    adjust_tree_values()
