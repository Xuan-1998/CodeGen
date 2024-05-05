def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    memo = {}
    def dp(x, y, prev_a):
        if (x, y, prev_a) in memo:
            return memo[(x, y, prev_a)]
        
        if x <= 0 or x > n:
            return -1
        
        if prev_a == a[-1]:
            return dp(1, 0, a[-1])
        
        new_x = x + prev_a
        new_y = y + prev_a
        if new_x <= 0 or new_x > n:
            return -1
        
        result = dp(new_x, new_y, prev_a)
        memo[(x, y, prev_a)] = result
        return result
    
    return str(dp(1, 0, a[1]))
