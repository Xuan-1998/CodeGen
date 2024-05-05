from collections import defaultdict
MOD = 10**9 + 7

def solve():
    n, s = [int(x) for x in input().split()]
    a = list(map(int, input().split()))
    dp = [[0]*(n+1) for _ in range(n+1)]
    memo = defaultdict(int)
    
    def dfs(i, j):
        if (i, j) not in memo:
            if i == j: 
                res = 1
            else:
                for k in range(j, i):
                    if all(a[ord(c)-97] >= ord(s[k]-97)//c+1 for c in set(s[k:j+1])):
                        res += dp[k][j-1]
                memo[(i, j)] = res % MOD
        return memo[(i, j)]
    
    res = 0
    for i in range(n):
        if all(a[ord(c)-97] >= ord(s[i]-97)//c+1 for c in set(s[i:i+n])):
            res += dfs(i, n-1)
    print(res)
    print(max(len(s[:i]) for i in range(n) if all(a[ord(c)-97] >= ord(s[:i].translate(str.maketrans("","").join(set(s[:i]))).translate(str.maketrans("","").join(set(s[:i])))[c-1]-97)//c+1 for c in set(s[:i]))))
    print(min(i+1 for i in range(n) if all(a[ord(c)-97] >= ord(s[:i].translate(str.maketrans("","").join(set(s[:i]))).translate(str.maketrans("","").join(set(s[:i])))[c-1]-97)//c+1 for c in set(s[:i]))))
