def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    m = int(input())
    prime_factors = list(map(int, input().split()))
    product = 1
    for p in prime_factors:
        product *= p

    max_distribution_index = 0
    for edge in edges:
        u, v = edge
        if (u == 1 and v == n) or (v == 1 and u == n):
            continue
        if u > v:
            u, v = v, u
        for i in range(u + 1, v):
            product //= prime_factors[i - 1]
            max_distribution_index += product

    print(max_distribution_index % (10**9 + 7))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
