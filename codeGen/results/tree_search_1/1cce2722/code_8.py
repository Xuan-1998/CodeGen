# Read the input
n = int(input())
a = list(map(int, input().split()))

# Count the frequency of each element
max_value = max(a)
count = [0] * (max_value + 1)
for number in a:
    count[number] += 1

# Initialize the dp array
dp = [0] * (max_value + 1)
dp[1] = count[1]

# Iterate over the range from 1 to the maximum element value and fill the dp array
for i in range(2, max_value + 1):
    dp[i] = max(dp[i-1], dp[i-2] + i * count[i])

# The answer will be the last element in the dp array
print(dp[max_value])
