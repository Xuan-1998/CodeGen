from collections import Counter
import sys

def max_points(sequence):
    max_val = max(sequence)
    freq = Counter(sequence)
    dp = [0] * (max_val + 1)
    dp[1] = freq[1]

    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * freq[i])
    
    return dp[max_val]

def main():
    n = int(sys.stdin.readline().strip())
    sequence = list(map(int, sys.stdin.readline().strip().split()))
    print(max_points(sequence))

if __name__ == "__main__":
    main()
