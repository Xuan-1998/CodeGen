import sys

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, a, b):
    x = find(parent, a)
    y = find(parent, b)

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def bit_xor_values(values):
    xor_sum = values[0]
    for value in values[1:]:
        xor_sum ^= value
    return xor_sum

n, k = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(n)]
rank = [0] * n

deleted_edges = 0
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    if find(parent, u) != find(parent, v):
        if deleted_edges >= k:
            print("NO")
            break
        union(parent, rank, u, v)
        deleted_edges += 1

if deleted_edges < k:
    xor_sums = {}
    for i in range(n):
        parent[i] = i
    for i in range(1, n):
        for edge in range(i - 1, -1, -1):
            if find(parent, edge) != find(parent, i):
                break
        else:
            xor_sum = bit_xor_values(values[edge:i + 1])
            if xor_sum not in xor_sums:
                xor_sums[xor_sum] = [edge]
            else:
                xor_sums[xor_sum].append(edge)
    if len(xor_sums) > 1 or (len(xor_sums) == 1 and len(xor_sums[list(xor_sums.keys())[0]]) > k):
        print("NO")
    else:
        print("YES")
else:
    print("YES")
