import sys

def solve():
    n = int(sys.stdin.readline())
    edges = []
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))

    m = int(sys.stdin.readline())
    prime_factors = list(map(int, sys.stdin.readline().split()))

    labels = [0] * (n-1)
    for i in range(n-1):
        u, v = edges[i]
        # Find the largest prime factor that divides both k and the product of all labels on the simple path
        k_product = 1
        for j in range(i+1):
            k_product *= labels[j]
        max_prime_factor = -1
        for p in prime_factors:
            if k % p == 0 and k_product % p == 0:
                max_prime_factor = max(max_prime_factor, p)
        labels[i] = max_prime_factor

    distribution_index = 0
    for i in range(n-1):
        u, v = edges[i]
        f_uv = sum(labels[j] for j in range(min(i+1, n-1), max(u+1, v)))
        distribution_index += f_uv

    print(distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
