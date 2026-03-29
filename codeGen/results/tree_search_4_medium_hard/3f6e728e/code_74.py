from collections import defaultdict

def solve():
    T = int(input())
    dp = defaultdict(int)
    dp[0] = 1
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        upper_radii = list(map(int, input().split()))
        lower_radii = list(map(int, input().split()))
        
        for radius in set(upper_radii + lower_radii):
            dp[radius] = (dp.get(radius-1, 0) * C - radius) % (10**9+7)
        
        print(' '.join(str(dp[i]) for i in range(C)))

solve()
