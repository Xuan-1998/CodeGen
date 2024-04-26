from collections import Counter
import sys

def max_points(sequence):
    frequency = Counter(sequence)
    max_element = max(sequence)
    dp = [0] * (max_element + 1)
    
    dp[1] = frequency[1]
    
    for i in range(2, max_element + 1):
        dp[i] = max(dp[i-1], i * frequency[i] + dp[i-2])
    
    return dp[max_element]

def main():
    n = int(input().strip())
    sequence = list(map(int, input().strip().split()))
    print(max_points(sequence))

if __name__ == "__main__":
    main()
