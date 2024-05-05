import sys

n = int(input())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

m = int(input())
prime_factors = list(map(int, input().split()))

k = multiply(prime_factors)

labels = [0] * (n + 1)
for edge in edges:
    u, v = edge
    dfs(u, -1)

distribution_index = sum(range(1, n))
f = lambda i, j: labels[i] if i < j else labels[j]

result = 0
for i in range(1, n):
    for j in range(i + 1, n):
        result += f(i, j)

print(result % (10 ** 9 + 7))
