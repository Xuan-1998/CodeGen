def max_points(n, sequence):
    if n == 0:
        return 0

    max_val = 105
    count = [0] * (max_val + 1)

    # Step 1: Populate the count array
    for num in sequence:
        count[num] += 1

    # Step 2: Initialize the dp array
    dp = [0] * (max_val + 1)
    dp[1] = count[1] * 1

    # Step 3: Fill the dp array using the state transition relation
    for x in range(2, max_val + 1):
        dp[x] = max(dp[x-1], dp[x-2] + count[x] * x)

    # Step 4: The result is the value of dp[max_val]
    return dp[max_val]

# Reading input from stdin
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
sequence = list(map(int, data[1:]))

# Output the result
print(max_points(n, sequence))

