def solve():
    q = int(input())
    dp = {0: True}

    for _ in range(q):
        u, v = map(int, input().split())
        and_u_v = u & v

        if and_u_v not in dp:
            dp[and_u_v] = dp[u ^ v]

        print("YES" if dp[and_u_v] else "NO")

solve()
