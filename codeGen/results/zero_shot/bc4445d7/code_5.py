import math

n = int(input())
edges = []
for i in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

m = int(input())
prime_factors = [int(x) for x in input().split()]

tree = {}
for edge in edges:
    u, v = edge
    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    tree[u].append(v)
    tree[v].append(u)

root = [node for node in tree if len(tree[node]) == 0][0]

labels = [0] * (n - 1)
for i in range(m):
    for j in range(n - 1):
        labels[j] += math.log(prime_factors[i], 2)

min_ones = sum(labels) // (n - 1)
labels = [(label + min_ones) % (n - 1) for label in labels]

max_distribution_index = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        sum_path = sum(labels[k] for k in range(i) if tree[i][k] == j)
        max_distribution_index += sum_path

print(max_distribution_index % (10**9 + 7))
