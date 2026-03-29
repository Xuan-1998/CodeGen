import heapq
from collections import defaultdict

def solve():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))

    k = int(input())
    primes = list(map(int, input().split()))
    m = len(primes)

    tree = defaultdict(dict)
    for u, v in edges:
        tree[u][v] = 1
        tree[v][u] = 1

    pq = [(0, n-1)]
    res = [0]
    while pq:
        f, node = heapq.heappop(pq)
        if len(tree[node]) == 0:
            continue
        for v in tree[node]:
            g = (f + 1) * primes[0] // (primes[0] - 1) ** (m-1)
            heapq.heappush(pq, (g, v))
        res.append(f)

    print(sum(res) % (10**9+7))

solve()
