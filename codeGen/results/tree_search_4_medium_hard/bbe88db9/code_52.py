def solve():
    n = int(input())
    portals = list(map(int, input().split()))
    memo = {}

    def dfs(i):
        if i == n+1:
            return 0
        if i not in memo:
            p_i_odd = sum(dfs(p) | (p % 2)) for p in portals[i-1:i])
            p_i_even = sum(dfs(p) & ~(p % 2)) for p in portals[i-1:i]))
            memo[i] = ((p_i_odd + p_i_even) % 1000000007)
        return memo[i]

    print(dfs(1))

solve()
