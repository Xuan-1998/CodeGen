n = int(input())  # Read the number of integers in the sequence
a = list(map(int, input().split()))  # Read the sequence

dp = [[0] * n for _ in range(n)]  # Initialize the DP table

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            dp[i][j] = 0
        else:
            delete_i = dp[(i-1)%n][max(0, j-2)] + (a[i] - a[j])  # Delete element at index i
            keep_i = dp[(i-1)%n][min(n-1, j+1)]  # Do not delete element at index i
            dp[i][j] = max(delete_i, keep_i)  # Update the maximum number of points

print(max(max(row) for row in dp))  # Find the maximum number of points that can be earned
