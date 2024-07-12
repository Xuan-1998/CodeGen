python
import sys

def max_points(n, sequence):
    # Frequency array
    count = [0] * 106  # Since ai is in the range 1 to 105

    # Populate the frequency array
    for num in sequence:
        count[num] += 1

    # DP array
    dp = [0] * 106

    # Base cases
    dp[0] = 0
    dp[1] = count[1] * 1

    # Fill the dp array using the transition relation
    for x in range(2, 106):
        dp[x] = max(dp[x-1], dp[x-2] + count[x] * x)

    # The answer is the maximum points we can get considering all integers up to 105
    return dp[105]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    
    result = max_points(n, sequence)
    print(result)

