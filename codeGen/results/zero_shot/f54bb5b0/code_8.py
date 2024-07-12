python
import sys
from collections import defaultdict, deque

input = sys.stdin.read
sys.setrecursionlimit(100000)

def count_pairs_with_path_length_k(n, k, edges):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    result = 0
    
    def dfs(node, parent):
        nonlocal result
        count = [0] * (k + 1)
        count[0] = 1
        
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            sub_count = dfs(neighbor, node)
            for i in range(k):
                result += count[i] * sub_count[k - i - 1]
            for i in range(k):
                count[i + 1] += sub_count[i]
        
        return count
    
    dfs(1, -1)
    return result

def main():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for i in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    result = count_pairs_with_path_length_k(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

