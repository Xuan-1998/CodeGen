from collections import Counter
import sys

def max_points(n, sequence):
    count = Counter(sequence)
    max_value = max(sequence)
    dp = [0] * (max_value + 1)

    for i in range(1, max_value + 1):
        if i == 1:
            dp[i] = count[i] * i
        else:
            dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)
    
    return dp[max_value]

if __name__ == "__main__":
    n = int(input().strip())
    sequence = list(map(int, input().strip().split()))
    print(max_points(n, sequence))
