# Read the input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Initialize dp array with zeros
dp = [[0 for _ in range(3)] for _ in range(n + 1)]

# Base case: no hares fed
for i in range(n):
    dp[i][0] = sum(c[:i+1])

# Recursive formula:
for i in range(n):
    for j in range(min(i, n - i)):
        # If left adjacent is full and right adjacent is hungry
        if j == 0: 
            dp[i][j+1] = max(dp[i-1][0], a[i])
        elif j == i:
            dp[i][j+1] = max(dp[i-1][i], c[i])
        else:
            dp[i][j+1] = max(dp[i-1][j-1], b[i])

# Print the maximum total joy
print(max(dp[-1]))
