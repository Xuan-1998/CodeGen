import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def max_distribution_index(edges, k_factors):
    labels = []
    product = 1
    for factor in k_factors:
        product *= factor
        labels.append(product)
    total_sum = sum(sum(labels[:i] + labels[i:]) for i in range(1, len(edges)))
    return total_sum % (10**9 + 7)

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        edges = []
        for _ in range(n - 1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
        m = int(sys.stdin.readline())
        k_factors = list(map(int, sys.stdin.readline().split()))
        print(max_distribution_index(edges, k_factors))

if __name__ == "__main__":
    main()
