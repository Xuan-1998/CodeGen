def can_form_polygon():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(n):
        if moods[i]:
            if i % 2 == 0:
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] = any(dp[j] for j in range(i))
    
    print("YES" if dp[-1] else "NO")

can_form_polygon()
