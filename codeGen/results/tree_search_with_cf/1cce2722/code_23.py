python
import sys
input = sys.stdin.read

def max_points(n, sequence):
    # Frequency array
    count = [0] * 106
    for num in sequence:
        count[num] += 1

    # DP array
    dp = [0] * 106
    dp[0] = 0
    dp[1] = count[1]

    # Fill the dp array using the recurrence relation
    for i in range(2, 106):
        dp[i] = max(dp[i-1], dp[i-2] + i * count[i])

    # The result is the maximum points that can be obtained
    return dp[105]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    print(max_points(n, sequence))

