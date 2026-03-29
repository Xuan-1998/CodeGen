import math

def calculate_probability():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    if sum(s) < n:
        return -1.0
    
    # Calculate the probability that a randomly formed team with k players will have at least one player from the department of interest
    dp = [0] * (n + 1)
    for i in range(h, n + 1):
        dp[i] = 1 - math.pow(1 - s[h-1]/sum(s), i-h+1)
    
    # Use binary search to find the minimum number of players needed for a team to have at least one player from the department of interest
    left, right = h, n
    while left < right:
        mid = (left + right) // 2
        if dp[mid] >= 0.5:
            right = mid
        else:
            left = mid + 1
    
    # Calculate and print the probability that a randomly formed team will have at least one player from the department of interest
    return min(1, dp[left])

print(calculate_probability())
