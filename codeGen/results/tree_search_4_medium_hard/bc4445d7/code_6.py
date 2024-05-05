def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    m = int(input())
    primes = list(map(int, input().split()))
    k = 1
    for p in primes:
        k *= p

    memo = [[float('inf')] * n for _ in range(n)]

    def dfs(i):
        if i >= len(edges):
            return 0
        u, v = edges[i]
        if memo[u][v] != float('inf'):
            return memo[u][v]
        prod = (n-1) // (v-u+1)
        if (n-1) % (v-u+1) == 0:
            memo[u][v] = min(dfs(u), dfs(v)) + prod
        else:
            memo[u][v] = float('inf')
        return memo[u][v]

    max_dist = 0
    for i in range(n):
        for j in range(i+1, n):
            if k % (j-i+1) == 0 and dfs(i) + dfs(j) >= k:
                max_dist += k // (j-i+1)
    print(max_dist % (10**9 + 7))

if __name__ == '__main__':
    solve()
