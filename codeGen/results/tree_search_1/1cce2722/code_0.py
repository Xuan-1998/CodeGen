from collections import Counter
import sys

def main():
    # Reading the input
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    
    # Step 1: Count the occurrences of each element
    occurrences = Counter(a)
    max_element = max(a)
    
    # Step 2: Initialize the dynamic programming array
    dp = [0] * (max_element + 1)
    
    # Step 3: Fill in the dynamic programming array
    for i in range(1, max_element + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + i * occurrences[i])
    
    # Step 4: Output the result
    print(dp[max_element])

if __name__ == "__main__":
    main()
