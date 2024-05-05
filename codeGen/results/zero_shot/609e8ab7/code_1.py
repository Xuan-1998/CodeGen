import sys

def read_input():
    n = int(input())
    p = [int(x) for x in input().split()]
    l, r = [], []
    for _ in range(n):
        l.append(int(x) for x in input().split())
        r.append(int(x) for x in input().split())
    return n, p, l, r

def build_tree(p, n):
    tree = [0] * (n + 1)
    for i in range(2, n + 1):
        tree[i] = i
    for i in range(n - 1, 1, -1):
        if p[i] != 0:
            tree[p[i]] = i
    return tree

def dfs(tree, l, r, node):
    max_val = 0
    for child in range(2 * node + 1, 2 * node + len(r) + 1):
        if child <= n and tree[child] != 0:
            max_val = max(max_val, dfs(tree, l, r, child))
    return max(l[node - 1], r[node - 1]) + max_val

def calculate_operations(n, p, l, r):
    operations = 0
    for i in range(1, n + 1):
        max_val = dfs(p, l, r, i)
        operations += ((max_val - l[i - 1]) // (r[i - 1] - l[i - 1] + 1)) + 1
    return operations

n, p, l, r = read_input()
print(calculate_operations(n, p, l, r))
