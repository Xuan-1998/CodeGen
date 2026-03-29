def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n):
        if all(mood == 1 for mood in moods[:i+1]):
            dp[i] = dp[i-1]
    
    print("YES" if dp[-1] else "NO")

can_form_polygon()
