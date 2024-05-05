import sys

n = int(input())  # Read the number of days
marks = list(map(int, input().split()))  # Read the number of marks strictly above the water on each day

dp = [0] * (n + 1)  # Initialize a dynamic programming array with n+1 elements

for i in range(1, n + 1):
    max_marks = max(marks[:i])  # Find the maximum number of marks strictly above the water level on previous days
    dp[i] = min(dp[j-1][max_marks] for j in range(i)) if i > 0 else 0  # Update the dynamic programming array

print(min(dp))  # Print the minimum possible sum of the number of marks strictly below the water level among all days
