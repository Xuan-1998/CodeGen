===BEGIN CODE===
def beautycontest(t, l, r):
    memo = {1: 0}
    
    def f(i):
        if i in memo:
            return memo[i]
        
        if i % 2 == 1:
            memo[i] = f((i + 1) // 2) + (i - (i - 1) // 2)
        else:
            memo[i] = min(f((i + 3) // 2), f(i - 1)) + 1
        
        return memo[i]
    
    res = sum(t * f(i) for i in range(l, r + 1)) - l * f(r)
    return pow(10**9 + 7, -1) * res % (10**9 + 7)

t, l, r = map(int, input().split())
print(beautycontest(t, l, r))
===END CODE===
