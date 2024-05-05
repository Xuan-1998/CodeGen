import sys

n = int(sys.stdin.readline())
edges = []
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

m = int(sys.stdin.readline())
prime_factors = list(map(int, sys.stdin.readline().split()))

product = 1
for p in prime_factors:
    product *= p

labels = [0] * (n-1)
for i in range(n-1):
    for j in range(i+1, n):
        f = 1
        path = [i]
        while path[-1] != j:
            for k in range(len(edges)):
                if edges[k][0] == path[-1]:
                    path.append(edges[k][1])
                    break
            f *= labels[k]
        f += labels[i]
        labels[f-1] += 1

max_distribution_index = sum((i+1) * (n-i-1) for i in range(n-2))
for i in range(1, n):
    max_distribution_index -= sum(labels[j] for j in range(i))

print(max_distribution_index % (10**9 + 7))
