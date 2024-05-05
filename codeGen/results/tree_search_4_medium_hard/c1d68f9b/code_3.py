def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(n):
        if moods[i] == 1:
            dp[i+1] = dp[i] or (i % 2 == 0)
        else:
            dp[i+1] = dp[i]
    
    return "YES" if dp[n] else "NO"

print(can_form_polygon())
