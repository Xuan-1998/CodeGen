def solve():
    n = int(input())
    moods = list(map(int, input().split()))
    
    dp = ["NO"] * (n + 1)
    dp[0] = "NO"
    dp[1] = "YES"
    
    for i in range(2, n):
        if sum(moods[:i+1]) % (i+1) == 0:
            dp[i] = "YES" if moods[i] == 1 else "NO"
        else:
            dp[i] = "NO"
    
    print("YES" if dp[-1] == "YES" else "NO")

solve()
