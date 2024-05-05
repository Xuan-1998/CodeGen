===BEGIN CODE===
def calculate_fare():
    n = int(input())
    
    # Initialize the DP table
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(n):
        t_i = int(input())
        
        if i == 0:
            for j in range(t_i):
                dp[i+1] = min(dp[i+1], dp[i] + 20)
        else:
            for j in range(i, -1, -1):
                if j >= t_i - 90:
                    dp[i+1] = min(dp[i+1], dp[j] + 50)
                elif j < t_i - 1:
                    dp[i+1] = min(dp[i+1], dp[j] + 20)
    
    print(dp[-1])

calculate_fare()
