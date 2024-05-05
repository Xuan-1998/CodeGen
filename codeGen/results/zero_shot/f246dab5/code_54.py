import sys

def calculate_fare():
    n = int(input())
    dp = [0] * (10**9 + 1)
    
    for _ in range(n):
        t_i = int(input())
        if dp[t_i] < 20:  # use one-trip ticket
            dp[t_i] += 20
        elif t_i >= 90:  # use 90-minute ticket
            dp[t_i] += 50
        else:
            dp[t_i] += 120  # use daily ticket
        
        for i in range(t_i, 10**9 + 1):
            if dp[i] < dp[i-1] + 20:  # use one-trip ticket
                dp[i] = dp[i-1] + 20
            elif i >= 90:
                dp[i] = min(dp[i], dp[i-1] + 50)  # use 90-minute ticket
            else:
                dp[i] = min(dp[i], dp[i-14*60] + 120)  # use daily ticket
        
        print(dp[t_i], end='\n')

calculate_fare()
