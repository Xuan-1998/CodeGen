import sys; input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    primes = list(map(int, input().split()))
    k = int(''.join(map(str, primes)))

    memo = {}

    def dfs(u):
        if u not in memo:
            memo[u] = (0, 0)
            for v, weight in edges:
                if v == u:
                    continue
                s, ones = dfs(v)
                memo[u] = ((memo[u][0] + weight) % k, (memo[u][1] + ones) % k)

        return memo[u]

    max_index = 0
    for _ in range(n-1):
        u, v = map(int, input().split())
        s, ones = dfs(u)
        max_index += s * ones

    print(max_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
