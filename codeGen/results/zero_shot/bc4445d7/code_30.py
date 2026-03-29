import sys

def find_prime_factors(n):
    prime_factors = []
    for p in range(2, int(n**0.5) + 1):
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        edges = []
        for _ in range(n-1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
        m = int(sys.stdin.readline())
        prime_factors = find_prime_factors(2*10**6)  # Assuming max value is 2*10^6
        k = 1
        for p in prime_factors[:m]:
            k *= p
        labels = []
        product = 1
        for edge in edges:
            u, v = edge
            if len(labels) == 0:
                labels.append(1)
            else:
                label = 1
                for i in range(len(labels)):
                    label *= labels[i]
                labels.append(k // label + (k % label > 0))
        distribution_index = sum(sum(range(i+1, n)) for i in range(n-1))
        print(distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
