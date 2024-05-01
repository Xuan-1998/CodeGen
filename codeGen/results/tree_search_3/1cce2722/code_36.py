from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    memo = defaultdict(int)
    
    max_points = 0
    
    for i in range(n):
        if i == 0:
            dp = [0] * (105 + 1)
        else:
            dp = [0] * (105 + 1)
            for j in range(105, -1, -1):
                dp[j] = max(dp[j], memo[(i - 1)] + (j == a[i]))
        
        for j in range(106):
            if i > 0:
                dp[j] = max(dp[j], dp[j])
            else:
                dp[j] = 0
        
        max_points = max(max_points, dp[105])
    
    print(max_points)

if __name__ == "__main__":
    solve()
