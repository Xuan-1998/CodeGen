from collections import defaultdict

def solve():
    n = int(input())
    dp = [[float('inf')] * 18001 for _ in range(90*60+1)]
    
    # Base case: when there are no more minutes left, 
    # the minimum cost is simply the total cost.
    for j in range(n):
        t = int(input())
        dp[0][j] = min(dp[0][j], 20)
        
    # Fill up the DP table
    for i in range(1, 90*60+1):
        for j in range(n):
            if i < t:
                dp[i][j] = min(dp[i][j], dp[0][j])
            elif i >= t + 89:
                dp[i][j] = min(dp[i][j], dp[0][j] + 120)
            else:
                dp[i][j] = min(dp[i][j], dp[0][j] + 50)
                
    # Print the minimum cost for each trip
    for j in range(n):
        t = int(input())
        print(min([dp[i][j] for i in range(t+1)]))

if __name__ == "__main__":
    solve()
