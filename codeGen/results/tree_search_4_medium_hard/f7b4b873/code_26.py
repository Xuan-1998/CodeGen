import sys

def partition_palindromic(s):
    n = len(s)
    dp = [[False] * (n+1) for _ in range(n+1)]
    
    # Single character is always palindromic
    for i in range(n+1):
        dp[i][i] = True
    
    # Check if the substring has matching characters
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if s[j] == s[i]:
                dp[j][i] = True
            elif i-j > 1:
                dp[j][i] = dp[j+1][i-1]
    
    # Create a list of palindromic partitions
    partitions = []
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                partition = s[i:j+1]
                while len(partition) > 0:
                    print(partition)
                    partition = partition[1:] + [partition[0]]
                    if ''.join(reversed(partition)) == ''.join(partition):
                        partitions.append(partition)
                        break
    return partitions

# Read the input string from stdin
s = sys.stdin.readline().strip()

# Solve the problem and print the result to stdout
print(partition_palindromic(s))
