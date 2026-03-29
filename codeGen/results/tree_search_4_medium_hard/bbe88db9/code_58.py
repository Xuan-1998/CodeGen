def solve(n, portals):
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Base case: we can't reach room j from room i if i > j
    for i in range(1, n+1):
        dp[i][i] = 1
    
    # Recursive function to calculate dp[i][j]
    def calc_dp(i, j):
        if i > j:
            return 0
        
        if dp[i][j]:
            return dp[i][j]
        
        if j == i: 
            return 1
        else: 
            odd_crosses = (i % 2) != 0
            portal_room = portals[i-1] if i > 1 else i+1
            
            # Calculate the number of ways to reach room j from room i
            dp[i][j] = calc_dp(i-1, portal_room) + (odd_crosses and 1 or 0)
            return dp[i][j]
    
    # Calculate the result
    return calc_dp(1, n+1) % MOD

# Example usage:
n = int(input())
portals = list(map(int, input().split()))
print(solve(n, portals))
