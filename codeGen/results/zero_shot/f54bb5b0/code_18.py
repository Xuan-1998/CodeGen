import sys
from collections import defaultdict, deque

input = sys.stdin.read
sys.setrecursionlimit(100000)

def count_pairs_with_path_length_k_in_tree(n, k, edges):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]

    def dfs(node, parent):
        dp[node][0] = 1
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for i in range(1, k + 1):
                result[0] += dp[node][i - 1] * dp[neighbor][k - i]
            for i in range(1, k + 1):
                dp[node][i] += dp[neighbor][i - 1]

    dfs(1, -1)
    return result[0]

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

    result = count_pairs_with_path_length_k_in_tree(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

