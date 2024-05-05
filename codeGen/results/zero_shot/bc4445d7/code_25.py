import sys
from collections import defaultdict

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, *edges = [int(x) for x in sys.stdin.readline().split()]
        m = int(sys.stdin.readline())
        primes = [int(x) for x in sys.stdin.readline().split()]
        k = 1
        for p in primes:
            k *= p
        
        dp = defaultdict(int)
        for u, v in edges:
            edge_label = 0
            for p in primes:
                if pow(p, edge_label, k) == (u ^ v):
                    break
                edge_label += 1
            
            dp[u] += edge_label
            dp[v] -= edge_label
        
        max_distribution_index = sum(abs(sum(dp[i:] for i in range(1, n))) for _ in range(n-1))
        print(max_distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
