import sys

def can_form_polygon():
    n = int(sys.stdin.readline())
    moods = list(map(int, sys.stdin.readline().split()))
    
    dp = [[False, False] for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n):
        if moods[i - 1]:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][0] or dp[i - 1][1]
        else:
            dp[i][0] = False
            dp[i][1] = dp[i - 1][0]
    
    print("YES" if dp[-1][1] else "NO")

can_form_polygon()
