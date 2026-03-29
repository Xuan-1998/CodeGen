def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        m = int(input())
        primes = list(map(int, input().split()))
        k = 1
        for p in primes:
            k *= p
        
        # Calculate the product of all integers that label the edges
        prod = 1
        for i in range(n-1):
            u, v = edges[i]
            # Label the edge with a number such that the product equals k
            # For simplicity, we use the smallest possible number
            prod *= min(u, v) + 1
        
        # Calculate the sum of all pairs of nodes
        dist_sum = 0
        for i in range(n-1):
            u, v = edges[i]
            dist_sum += (min(u, v) + 1) * (n - 2 - i)
        
        print(dist_sum % (10**9 + 7))

if __name__ == "__main__":
    solve()
