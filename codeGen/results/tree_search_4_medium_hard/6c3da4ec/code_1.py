def max_bitwise_or(n, s):
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    def f(i, j):
        if i == j:
            return int(s[i])
        res = 0
        for k in range(i):
            res = max(res, f(k, i-1) | int(s[i]))
        return res
    
    dp[0][0] = 0
    return f(0, n)

n = int(input())
s = input()
print(max_bitwise_or(n, s))
