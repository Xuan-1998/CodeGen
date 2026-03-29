def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for j in range(i):
                if sum(b[:j+1]) == i:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        print("YES" if dp[-1] != float('inf') else "NO")

can_send_over_network()
