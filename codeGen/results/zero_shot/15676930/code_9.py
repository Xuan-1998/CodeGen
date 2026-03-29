# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Initialize dp array with maximum value for each hare (n-1) times
dp = [0] * n

# Calculate the maximum joy for each hare considering its adjacent hares
for i in range(n):
    if i == 0:
        # First hare, only one option: feed it
        dp[i] = c[0]
    elif i == n - 1:
        # Last hare, only one option: don't feed it (max joy is the same as previous)
        dp[i] = dp[i-1]
    else:
        # Middle hares have three options: feed or not, considering adjacent hares
        dp[i] = max(c[i], a[i-1] + b[i], c[i-1] + c[i])

# Print the maximum total joy
print(max(dp))
