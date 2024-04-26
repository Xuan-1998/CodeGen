from collections import Counter
import sys

def main():
    # Read input
    n = int(input().strip())
    sequence = list(map(int, input().strip().split()))

    # Count the occurrences of each number in the sequence
    count = Counter(sequence)

    # The maximum number in the sequence is needed to construct the dp array
    max_num = max(sequence)

    # Initialize the dp array
    dp = [0] * (max_num + 1)

    # Base cases
    dp[1] = count[1] * 1

    # Build the dp array
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)

    # The answer is the last element in the dp array
    print(dp[max_num])

if __name__ == "__main__":
    main()
