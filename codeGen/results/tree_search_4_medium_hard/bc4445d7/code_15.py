import heapq
from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        
        k = int(input())
        primes = list(map(int, input().split()))
        prime_product = 1
        for p in primes:
            prime_product *= p
        
        dp = defaultdict(lambda: {(p, s): float('inf') for s in range(31)})
        pq = [(0, 0, 0)]
        
        for _ in range(n-1):
            u, v = heapq.heappop(pq)
            for p, s in [(u, v), (v, u)]:
                for new_p, new_s in [(p+1, s+1)] if p < k else [(p, s+1)]:
                    dp[u][v][new_p][new_s] = min(dp[u][v][new_p][new_s], dp[p][u][new_p][s]+(prime_product//p))
        
        ans = 0
        for u in range(1, n):
            for v in range(u+1, n):
                ans += dp[u][v][k][30]
        
        print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
