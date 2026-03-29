import sys

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    dp = {}

    def dfs(i):
        if i == 0:
            return 0
        if (i,) in dp:
            return dp[(i,)]
        res = float('inf')
        j = n - 1
        while j >= 0:
            k = strings[j].index(strings[i-1])
            res = min(res, costs[j] + dfs(i-1) + len(strings[i-1]) - k)
            j -= 1
        dp[(i,)] = res
        return res

    if n == 1:
        print(-1)
    else:
        res = dfs(n)
        print(res)

solve()
