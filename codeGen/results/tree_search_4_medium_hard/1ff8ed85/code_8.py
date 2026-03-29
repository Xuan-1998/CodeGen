def can_send_over_network():
    t = int(input())  # number of test cases

    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))

        dp = [[False] * (10**9 + 1) for _ in range(2*10**5 + 1)]

        prev_val = 0
        for i in range(n+1):
            if i > 0:
                prev_val = b[i-1]
            for j in range(max(prev_val, 1), min(10**9, prev_val+1)):
                dp[i][j] = any(dp[k][j-k] for k in range(i) if k > 0 and k <= i-1)
            if i == n:
                print("YES" if dp[n][b[n]] else "NO")
