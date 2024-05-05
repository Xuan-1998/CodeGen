import sys
from collections import defaultdict

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        edges = []
        for _ in range(n-1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
        m = int(sys.stdin.readline())
        primes = list(map(int, sys.stdin.readline().split()))
        k = 1
        for p in primes:
            k *= p

        # Calculate the distribution index
        dist_index = 0
        prime_counts = defaultdict(int)
        for u, v in edges:
            if u > v:
                u, v = v, u
            path_sum = k // (v - u + 1)
            dist_index += path_sum * (v - u) * (u - 1)
            for i in range(u, v):
                prime_counts[i] += 1

        print(dist_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
