from sys import stdin
from collections import defaultdict
from math import factorial

MOD = 998244353

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def add_edge(tree, u, v):
    tree[u].children.append(tree[v])
    tree[v].children.append(tree[u])

def find_centroid(tree, n):
    # Function to find the size of each subtree and check if a node is a centroid
    def dfs(node, parent):
        size[node] = 1
        is_centroid = True
        for child in node.children:
            if child == parent:
                continue
            dfs(child, node)
            size[node] += size[child]
            if size[child] > n // 2:
                is_centroid = False
        if n - size[node] > n // 2:
            is_centroid = False
        if is_centroid:
            centroids.append(node)

    size = {node: 0 for node in tree}
    centroids = []
    dfs(next(iter(tree)), None)  # Start DFS from any node
    return centroids[0]  # Return any centroid

def count_permutations(node, parent):
    # Count the number of permutations for the subtree rooted at 'node'
    count = 1
    size = 1
    for child in node.children:
        if child == parent:
            continue
        child_count, child_size = count_permutations(child, node)
        count = (count * child_count) % MOD
        count = (count * factorial(size + child_size - 1) // factorial(size - 1)) % MOD
        size += child_size
    return count, size

# Read input
n = int(stdin.readline())
tree = {i: TreeNode(i) for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    add_edge(tree, u, v)

# Find centroid and count permutations
centroid = find_centroid(tree, n)
answer, _ = count_permutations(centroid, None)
print(answer)
