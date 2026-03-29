def can_send_sequence():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = [True] + [False]*n
        for i in range(1, n+1):
            if b[i-1] % 2 == 0:
                dp[i] = dp[i-1]
            elif b[i-1] == len(a):
                dp[i] = dp[b[i-1]-1]
        print("YES" if dp[n] else "NO")

can_send_sequence()
