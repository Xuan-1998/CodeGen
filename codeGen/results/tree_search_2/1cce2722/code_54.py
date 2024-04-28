def max_points(a):
    n = len(a)
    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        
        if i < 2:
            return 0
        
        ans = 0
        for k in range(1, min(i, 105)):
            if a[i] - k not in a[:i]:
                ans = max(ans, dp(i-k-1) + (a[i]-k))
        
        memo[i] = ans
        return ans
    
    return dp(n)

# read input from standard input
n = int(input())
a = list(map(int, input().split()))

print(max_points(a))
