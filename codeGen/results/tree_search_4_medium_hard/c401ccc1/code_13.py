def is_path_exists():
    q = int(input())
    memo = {}

    def dfs(u, v):
        if (u, v) in memo:
            return memo[(u, v)]
        if u == v:
            return False
        if u > v:
            u, v = v, u
        for w in range(2**30):
            if u & w and not w and dfs(w, v):
                memo[(u, v)] = True
                return True
        memo[(u, v)] = False
        return False

    for _ in range(q):
        u, v = map(int, input().split())
        print("YES" if dfs(u, v) else "NO")
