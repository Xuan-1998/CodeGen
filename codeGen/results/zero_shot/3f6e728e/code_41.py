def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        upper_hemispheres = list(map(int, input().split()))
        lower_hemispheres = list(map(int, input().split()))
        
        dp = [0] * (C + 1)
        for i in range(1, C + 1):
            if len([radius for radius in upper_hemispheres if radius == i]) > 0:
                dp[i] += 1
            if len([radius for radius in lower_hemispheres if radius == i]) > 0:
                dp[i] += 1
        
        max_length = min(N, M)
        
        print(*dp[:max_length], sep=' ')

solve()
