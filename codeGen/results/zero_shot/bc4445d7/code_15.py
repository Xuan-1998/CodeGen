def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        
        m = int(input())
        prime_factors = list(map(int, input().split()))
        k = 1
        for p in prime_factors:
            k *= p
        
        # Precompute all prime numbers up to a certain limit
        sieve = [True] * (6*10**4 + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int((6*10**4)**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, 6*10**4 + 1, i):
                    sieve[j] = False
        
        # Label edges with prime factors
        edge_labels = [0] * (n-1)
        for i, (u, v) in enumerate(edges):
            label = next(p for p in prime_factors if p <= k // (6*10**4 + 1))
            edge_labels[i] = label
            k //= label
        
        # Calculate f(u,v) and distribution index
        distribution_index = 0
        for i, (u, v) in enumerate(edges):
            fuv = sum(edge_labels[:i+1])
            distribution_index += fuv * (n-1 - i)
        
        print(distribution_index % (10**9 + 7))

if __name__ == '__main__':
    solve()
