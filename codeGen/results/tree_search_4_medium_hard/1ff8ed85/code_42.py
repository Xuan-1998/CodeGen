t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    dp = [True]
    for i in range(1, n):
        if (b[i-1] % 2 == 0 and dp[i-1]) or (b[i-1] % 2 != 0 and not dp[i-1]):
            dp.append(True)
        else:
            dp.append(False)
    
    print("YES" if dp[-1] else "NO")
