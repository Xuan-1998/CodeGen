import sys
input = sys.stdin.read
from collections import defaultdict, deque

def count_pairs_with_distance_k(n, k, edges):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    def dfs(node, parent):
        dp = [0] * (k + 1)
        dp[0] = 1
        total_pairs = 0
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_dp, child_pairs = dfs(neighbor, node)
            total_pairs += child_pairs
            
            for i in range(k):
                total_pairs += dp[i] * child_dp[k - i - 1]
            
            for i in range(k):
                dp[i + 1] += child_dp[i]
        
        return dp, total_pairs
    
    _, result = dfs(1, -1)
    return result

def main():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    result = count_pairs_with_distance_k(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

