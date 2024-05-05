def infinite_zoo():
    q = int(input())
    dp = [False] * (2**30)
    dp[0] = True

    for _ in range(q):
        u, v = map(int, input().split())
        if dp[v]:  # Check if there's a path from 0 to v
            print("YES")
        else:
            print("NO")

infinite_zoo()
