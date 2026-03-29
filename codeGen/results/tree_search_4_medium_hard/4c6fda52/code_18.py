import sys

def process_query(n, k, s):
    # Initialize dp array with n+1 elements
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i < k:
            # For substrings of length less than k, count the number of characters that need to be changed
            dp[i] = sum(s[:i] != 'RGB'[i % 3])
        else:
            # For substrings of length k, check if the last character needs to be changed
            dp[i] = min(dp[i - 1] + (s[i - k:i] != 'RGB'[k % 3]), 
                        dp[max(0, i - k)] + (s[i - 1] != 'RGB'[i % 3]))
    
    return dp[n]

while True:
    try:
        n, k = map(int, input().split())
        s = input()
        
        # Process the query and print the answer
        print(process_query(n, k, s))
    except EOFError:
        break
