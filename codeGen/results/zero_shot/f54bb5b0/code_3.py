import sys
input = sys.stdin.read
from collections import defaultdict, deque

def count_pairs_with_k_distance(n, k, edges):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    def dfs(node, parent):
        count = [0] * (k + 1)
        count[0] = 1
        total_pairs = 0
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_count, child_pairs = dfs(neighbor, node)
            total_pairs += child_pairs
            
            for i in range(k):
                total_pairs += count[i] * child_count[k - i - 1]
            
            for i in range(k):
                count[i + 1] += child_count[i]
        
        return count, total_pairs
    
    _, result = dfs(1, -1)
    return result

def main():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        ai = int(data[index])
        bi = int(data[index + 1])
        edges.append((ai, bi))
        index += 2
    
    result = count_pairs_with_k_distance(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

