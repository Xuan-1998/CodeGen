import sys
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)

    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))

    memo = {i: [0, 0] for i in range(n + 1)}

    def dfs(i):
        if i == t:
            return [0, 0]
        if memo[i][0]:
            return memo[i]
        ret = [float('inf'), -1]
        for j in g[i]:
            if j not in path[:k] and j != t:
                rec = [x + 1 for x in dfs(j)]
                min_rec, max_rec = min(rec[0], ret[0]), max(rec[0], ret[1])
                if i != s:
                    ret[0] = min(ret[0], 1 + min_rec)
                    ret[1] = max(ret[1], 1 + max_rec)
        memo[i] = ret
        return ret

    res = dfs(s)
    print(*res)

if __name__ == "__main__":
    main()
