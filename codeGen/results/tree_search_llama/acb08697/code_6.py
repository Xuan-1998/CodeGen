def min_stones(n, s):
    # Initialize a list to store the minimal possible number of stones in the pile after each operation
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if s[i - 1] == '+':
            # If the current operation is adding one stone, update the state variable accordingly
            dp[i] = max(dp[i - 1], dp[i - 1] + 1)
        else:
            # If the current operation is removing one stone, update the state variable accordingly
            dp[i] = min(dp[i - 1], dp[i - 1] - 1)
    
    return dp[n]

n = int(input())
s = input()
print(min_stones(n, s))
