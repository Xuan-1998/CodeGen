import sys

def find_prime_factors(n):
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def calculate_distribution_index(edges, k):
    distribution_index = 0
    for edge in edges:
        u, v = edge
        # Label the edge with a positive integer that contributes to the minimum possible number of 1s.
        label = 1
        if len(set(edge)) == 2:  # If it's an internal edge (not the root node)
            label += k // (u + 1)  # Calculate the label based on the prime factors of k
        distribution_index += label * (v - u)
    return distribution_index

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, edges = [int(x) for x in sys.stdin.readline().split()]
        m = int(sys.stdin.readline())
        prime_factors = find_prime_factors(m)
        k = 1
        for p in prime_factors:
            k *= p
        distribution_index = calculate_distribution_index(edges, k)
        print(distribution_index % (10**9 + 7))

if __name__ == "__main__":
    main()
