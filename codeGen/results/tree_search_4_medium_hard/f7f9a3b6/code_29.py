import sys

def solve(n, s, a):
    MOD = 10**9 + 7
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    
    # Base case: empty string
    dp[0][1] = 1
    
    for i in range(1, n+1):
        for j in range(min(i+1, len(s)+1), 0, -1):
            if s[i-1] not in set(s[:i]):
                dp[i][j] += dp[i-1][1]
            else:
                for k in range(min(j, i//a[ord(s[i-1])-ord('a')+1]), 0, -1):
                    dp[i][j] += dp[i-k][k]*a[ord(s[i-1])-ord('a')]
            
            dp[i][j] %= MOD
    
    # Calculate the number of ways to split s
    num_ways = dp[n][1]
    
    # Find the length of the longest substring
    max_length = 0
    for j in range(2, n+1):
        if dp[n][j]:
            max_length = j
    
    # Find the minimum number of substrings
    min_substrings = float('inf')
    for j in range(2, n+1):
        if dp[n][j]:
            min_substrings = min(min_substrings, j)
    
    return num_ways, max_length, min_substrings

n = int(input())
s = input()
a = [int(x) for x in input().split()]

num_ways, max_length, min_substrings = solve(n, s, a)

print(num_ways % (10**9 + 7))
print(max_length)
print(min_substrings)
