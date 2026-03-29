from collections import defaultdict

def find_optimal_capital(n):
    # Initialize DP array and memo dictionary
    dp = [float('inf')] * (n + 1)
    memo = defaultdict(int)

    # Calculate DP values using memoization
    for i in range(2, n + 1):
        for j in range(i + 1, n + 1):
            if memo[j] > memo[i]:
                dp[i] = min(dp[i], 1 + dp[j])
        memo[i] = dp[i]

    # Find the optimal capital
    max_in_degree = max(memo.values())
    optimal_capital = [i for i in range(2, n + 1) if memo[i] == max_in_degree][0]

    return dp[optimal_capital], str(optimal_capital)

# Example usage:
n = int(input())
dp, capital = find_optimal_capital(n)
print(dp)
print(capital)
