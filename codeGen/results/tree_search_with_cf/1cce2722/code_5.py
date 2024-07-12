python
import sys
input = sys.stdin.read

def max_points(n, sequence):
    if n == 0:
        return 0

    max_val = 105
    count = [0] * (max_val + 1)

    for num in sequence:
        count[num] += 1

    dp = [0] * (max_val + 1)
    dp[0] = 0
    dp[1] = count[1]

    for x in range(2, max_val + 1):
        dp[x] = max(dp[x-1], dp[x-2] + x * count[x])

    return dp[max_val]

# Read input
data = input().strip().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Calculate and print the result
print(max_points(n, sequence))

