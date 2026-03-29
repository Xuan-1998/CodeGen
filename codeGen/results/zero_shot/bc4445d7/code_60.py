import sys

def max_distribution_index(n, edges, m, prime_factors):
    # Step 2: Calculate the number of prime factors
    pass

    # Step 3: Find the prime factorization of k
    pass

    # Step 4: Construct a tree with n nodes using the given edges
    pass

    # Step 5: Calculate f(u, v) for each edge (u, v)
    pass

    # Step 6: Calculate the distribution index and sum them up
    pass

    return max_distribution_index % (10**9 + 7)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = [(int(x), int(y)) for x, y in [line.split() for line in sys.stdin.read().splitlines()][1:]]
        m = int(input())
        prime_factors = list(map(int, input().split()))
        print(max_distribution_index(n, edges, m, prime_factors))
