def dp(s):
    if dp_cache.get(s) is not None:
        return dp_cache[s]
    
    if s == 0:  # base case: no more elements to delete
        return 0
    
    max_points = 0
    for i in range(max(1, a[s-1]), min(a[s]+2, n)):
        new_s = i - 1
        new_s_points = dp(new_s) + s - new_s
        max_points = max(max_points, new_s_points)
    
    dp_cache[s] = max_points
    return max_points

dp_cache = {}
n = int(input())
a = [int(x) for x in input().split()]
print(dp(n-1))
