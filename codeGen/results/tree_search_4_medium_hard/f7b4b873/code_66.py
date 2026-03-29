from collections import defaultdict

def partition_palindromes(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # All substrings with one character are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Fill up the dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if the left and right parts are palindromes
            if s[i] == s[j] and (length == 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
    
    def get_partitions(s):
        partitions = [[]]
        
        for i in range(len(s)):
            new_partitions = []
            
            # Iterate through each partition
            for j, partition in enumerate(partitions):
                k = len(partition)
                
                if s[k:i+1] and dp[k][i]:
                    new_partitions.append(partition + [s[k:i+1]])
                    
                else:
                    new_partitions.append(partition + [s[i]])
            
            partitions = new_partitions
        
        return partitions
    
    return get_partitions(s)

s = input()
print(partition_palindromes(s))
