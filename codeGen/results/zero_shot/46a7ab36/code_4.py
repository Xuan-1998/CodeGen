import sys

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the size of the alphabet and the length of each word
    n, m = map(int, input().split())
    
    # Initialize the dp array with 1 for the first character
    dp = [1] * (n + 1)
    
    # Calculate the number of possible words for each position in the word
    for i in range(2, n + 1):
        if i <= m:
            dp[i] = (dp[i - 1] * (i - 1) % (10**8 + 7)) * (n - i + 1) % (10**8 + 7)
        else:
            dp[i] = (dp[i - 2] * (i - 2) % (10**8 + 7)) * (n - i + 1) % (10**8 + 7)
    
    # Calculate the total number of possible words
    total_words = sum(dp[m:]) % (10**8 + 7)
    
    # Print the result
    print(total_words)
