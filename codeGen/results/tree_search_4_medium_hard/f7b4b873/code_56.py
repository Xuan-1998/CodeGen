from collections import defaultdict

def partition_palindromic(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    res = []
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i:j+1] == s[i:j+1][::-1]:
                dp[i][j] = True
                for k in range(j, n):
                    if dp[i][k-1] and s[k-n:k+1] == s[k-n:k+1][::-1]:
                        res.append([s[i:j+1]])
    
    return res

# Input the string from standard input
n = int(input())
s = [char for char in input().strip()]

print(partition_palindromic(s))
