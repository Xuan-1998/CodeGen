import sys

def read_input():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        edges = []
        for _ in range(n-1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
        m = int(sys.stdin.readline())
        prime_factors = list(map(int, sys.stdin.readline().split()))
        return n, edges, m, prime_factors

def calculate_distribution_index(n, edges, m, prime_factors):
    # TO DO: implement the calculation of distribution index
    pass

T = read_input()
for _ in range(T):
    n, edges, m, prime_factors = read_input()
    distribution_index = calculate_distribution_index(n, edges, m, prime_factors)
    print(distribution_index % (10**9 + 7))
