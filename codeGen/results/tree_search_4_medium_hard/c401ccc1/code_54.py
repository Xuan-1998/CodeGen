import sys

def solve():
    q = int(input())
    memo = {}

    for _ in range(q):
        u, v = map(int, input().split())
        if (u, v) not in memo:
            memo[(u, v)] = dfs(u)
        print("YES" if memo[(u, v)][v] else "NO")

def dfs(v):
    if v in memo:
        return memo[v]
    dp = [False] * 2**30
    for u in range(2**30):
        if u & v == v and not dp[u]:
            dp[u] = True
            for w in range(2**30):
                if (u & w) == w and dp[w]:
                    dp[w | v] = True
    memo[v] = dp
    return dp

if __name__ == "__main__":
    solve()
