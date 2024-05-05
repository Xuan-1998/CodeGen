def partition_palindromes(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Base case: single character palindromes are always True
    for i in range(n):
        dp[i][i] = True
    
    partitions = []
    
    def backtrack(start, end):
        if start > end:
            return
        
        for i in range(start, end + 1):
            if s[start:i+1] == s[i:end+1][::-1]:
                partitions.append(s[start:end+1])
                
                # Recursively generate all possible palindromic partitions
                backtrack(i+1, end)
    
    # Initialize the DP table and start backtracking from the last character to the first
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if the substring is a palindrome based on the previous state
            dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
    
    backtrack(0, n - 1)
    
    return partitions

# Example usage:
input_string = input()
print(partition_palindromes(input_string))
