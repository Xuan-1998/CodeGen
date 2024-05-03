def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        if dp[i - 1]:
            if i % 2 == 0:  # decrement from the end
                dp[i] = all(x <= 0 for x in arr[:i])
            else:  # decrement from the beginning
                dp[i] = all(x <= 0 for x in arr[i-1:])
        else:
            dp[i] = False
    
    print("YES" if dp[-1] else "NO")
