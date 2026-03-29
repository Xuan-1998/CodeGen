def f(s, k):
    if k == 1:
        return s[0] if s else ''
    
    dp = [''] * (k + 1)
    for i in range(k + 1):
        for j in range(len(s)):
            if i > 0 and (i == len(s) or s[j] != s[-1]):
                dp[i] += s[j]
            elif i <= len(s) // 2:
                dp[i] = min(dp[i], f(s[:j+1], i))
    
    return dp[k]

n, k = map(int, input().split())
s = input()
print(f(s, k))
