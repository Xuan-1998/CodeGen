import math

def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    m = int(input())
    prime_factors = [int(x) for x in input().split()]

    labeled_edges = {}
    product = 1
    for p in prime_factors:
        product *= p

    for edge in edges:
        u, v = edge
        if (u, v) not in labeled_edges:
            labeled_edges[(u, v)] = min((product // p) ** -1 for p in prime_factors)
            product //= labeled_edges[(u, v)]
        else:
            continue

    distribution_index = sum(sum(f(i, j) for j in range(i + 1, n)) for i in range(n - 1))
    print(distribution_index % (10**9 + 7))

if __name__ == '__main__':
    solve()
