import sys

def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = [-1] * (n + 1)
        prev_val = 0
        for i in range(n):
            for j in range(1, b[i] + 1):
                if j <= b[i] - prev_val:
                    dp[b[i]] = 1
                else:
                    dp[b[i]] = 0
                prev_val = b[i]
        
        print('YES' if dp[-1] == 1 else 'NO')

can_send_over_network()
