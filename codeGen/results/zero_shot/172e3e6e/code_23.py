# Step 1: Read input
n = int(input())
a = list(map(int, input().split()))

# Initialize dp array
dp = [0] * (n + 1)

# Fill up dp array
for i in range(1, n + 1):
    # Code to calculate dp[i]
    pass

# Calculate the number of good subsequences
num_good_subsequences = 0
for i in range(n - 1, -1, -1):
    if (a[i] % (i + 1) == 0 and dp[i + 1]):
        num_good_subsequences += 1

print(num_good_subsequences % (10**9 + 7))
