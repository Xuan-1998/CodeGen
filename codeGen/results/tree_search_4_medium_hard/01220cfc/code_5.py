from sys import stdin

def canJump(arr):
    n = len(arr)
    dp = [True] * (n+1)  # Initialize DP states with all True
    dp[0] = False  # Start at the beginning, so it's impossible to reach the start

    for i in range(1, n):
        if not dp[i-1]:  # If you can't reach the previous index
            continue
        j = min(i+arr[i], n) - 1  # Find the maximum reachable index
        for k in range(j, -1, -1):  # Iterate through all indices that can be reached
            if not dp[k]:  # If you can't reach this index
                break
            j = k  # Update the maximum reachable index
        dp[i] = True if j >= n-1 else False  # Check if it's possible to reach the end

    return dp[-1]

arr = list(map(int, stdin.readline().split()))
print(canJump(arr))
