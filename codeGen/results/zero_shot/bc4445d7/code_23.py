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
        
        yield n, edges, m, prime_factors

def solve_case(n, edges, m, prime_factors):
    # Step 1: Calculate the product of all prime factors
    k = 1
    for p in prime_factors:
        k *= p
    
    # Step 2: Find the maximum possible distribution index
    max_distribution_index = 0
    for u, v in edges:
        f_uv = 1
        for i in range(m):
            if u < v and prime_factors[i] <= (v - u + 1) // (n-1):
                f_uv *= prime_factors[i]
            elif v < u and prime_factors[i] <= (u - v + 1) // (n-1):
                f_uv *= prime_factors[i]
        
        max_distribution_index += sum(range(f_uv+1))
    
    # Step 3: Print the answer modulo 10^9 + 7
    print(max_distribution_index % (10**9 + 7))

for case in read_input():
    solve_case(*case)
