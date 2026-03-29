def infinite_zoo(q):
    memo = {}
    for _ in range(q):
        u, v = map(int, input().split())
        if (v & u) == v:
            print("NO")
            continue
        dp = [[False] * (1 << 30) for _ in range(1 << 30)]
        for w in range(1 << 30):
            if (u & w) != w:
                dp[u][w] = True
        while v != u:
            for w in range(1 << 30):
                if (v & w) == w and dp[v][w]:
                    dp[u][w] = True
                    break
            if not dp[u][v]:
                print("NO")
                break
        else:
            print("YES")

if __name__ == "__main__":
    q = int(input())
    infinite_zoo(q)
