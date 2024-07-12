import sys
from collections import defaultdict, deque

input = sys.stdin.read

def count_pairs_with_path_length_k(n, k, edges):
    # Create adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    # Function to perform DFS and count distances
    def dfs(node, parent):
        dist_count = defaultdict(int)
        dist_count[0] = 1  # Distance from node to itself is 0
        total_pairs = 0

        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            child_dist_count, child_pairs = dfs(neighbor, node)
            total_pairs += child_pairs

            # Count pairs with the current node as LCA
            for d1 in dist_count:
                if k - d1 - 1 in child_dist_count:
                    total_pairs += dist_count[d1] * child_dist_count[k - d1 - 1]

            # Merge child's distances into current node's distances
            for d in child_dist_count:
                dist_count[d + 1] += child_dist_count[d]

        return dist_count, total_pairs

    # Start DFS from any node, here we choose node 1
    _, result = dfs(1, -1)
    return result

def main():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2

    result = count_pairs_with_path_length_k(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

