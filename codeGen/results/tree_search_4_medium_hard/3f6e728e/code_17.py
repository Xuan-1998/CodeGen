def solve():
    t = int(input())
    for _ in range(t):
        n, m, c = map(int, input().split())
        u_rads = list(map(int, input().split()))
        l_rads = list(map(int, input().split()))
        
        dp = [0] * (c + 1)
        dp[0] = 1
        
        for i in range(1, c + 1):
            count = sum(1 for j in range(min(i, len(u_rads))) if u_rads[j] <= i) or 0
            count += sum(1 for j in range(min(i, len(l_rads))) if l_rads[j] <= i) or 0
            
            if count > 0:
                dp[i] = (dp[i - 1] * count) % (10**9 + 7)
        
        print(*map(str, dp), sep=' ')
