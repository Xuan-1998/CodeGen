from collections import defaultdict
from math import factorial
from sys import stdin, stdout

MOD = 998244353

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_edge(tree, u, v):
    tree[u].children.append(tree[v])
    tree[v].children.append(tree[u])

def find_centroid(tree, n):
    # Function to find the centroid of the tree
    def dfs(node, parent):
        size[node.value] = 1
        max_subtree_size = 0
        for child in node.children:
            if child.value != parent and not visited[child.value]:
                subtree_size = dfs(child, node.value)
                max_subtree_size = max(max_subtree_size, subtree_size)
                size[node.value] += subtree_size
        max_subtree_size = max(max_subtree_size, n - size[node.value])
        if max_subtree_size <= n // 2:
            centroids.append(node)
        return size[node.value]

    size = [0] * (n + 1)
    visited = [False] * (n + 1)
    centroids = []
    dfs(tree[1], -1)
    return centroids[0]

def count_permutations(tree, n):
    # Function to count the number of valid permutations
    def dfs_count(node, parent):
        count = 1
        fact = 1
        for child in node.children:
            if child.value != parent:
                subtree_count = dfs_count(child, node.value)
                count *= subtree_count
                count %= MOD
                fact *= factorial(len(child.children))
                fact %= MOD
        return count * pow(fact, MOD - 2, MOD) % MOD

    centroid = find_centroid(tree, n)
    result = dfs_count(centroid, -1)
    result *= factorial(n)
    result %= MOD
    return result

# Read input
n = int(stdin.readline())
tree = {i: TreeNode(i) for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    add_edge(tree, u, v)

# Calculate and output the result
result = count_permutations(tree, n)
stdout.write(str(result) + '\n')
