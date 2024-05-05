import sys

def solve(s, a):
    n = len(s)
    dp = [[0] * (sum(a) + 1) for _ in range(n+1)]
    
    total_count = 0
    max_length = 0
    min_count = float('inf')
    
    last_split = -1
    
    for i in range(1, n+1):
        for j in range(sum(a), 0, -1):
            if dp[i-1][j]:
                k = s[i-1].count(s[i-1])
                if k <= a[ord(s[i-1]) - ord('a')]:
                    dp[i][j-k] = True
                else:
                    break
            elif j > 0 and (last_split == -1 or s[i-1] != s[last_split]):
                for k in range(j, 0, -1):
                    if dp[i-1][k] and all(s[i-x-1].count(c) <= a[ord(c) - ord('a')] for c in set(s[i-x-1])):
                        dp[i][j-k] = True
                        break
            last_split = i-1
    
    for j in range(sum(a), 0, -1):
        if dp[n][j]:
            total_count += 1
            max_length = max(max_length, j)
            min_count = min(min_count, 1 + (n-j)//(sum(a)-j))
    
    print((total_count % (10**9 + 7)) or 1)
    print(max_length)
    print(min_count)

s = input()
a = [int(x) for x in input().split()]
solve(s, a)
