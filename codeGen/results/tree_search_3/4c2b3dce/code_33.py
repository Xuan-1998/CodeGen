def solve():
    n = int(input())
    s = input().strip()
    
    dp = [[False, False] for _ in range(n+1)]
    
    for i in range(n):
        if s[i] == 'A':
            dp[i+1][0] = True
        elif s[i] == 'B':
            dp[i+1][1] = True
    
    found_ab = any([dp[i][0] and dp[j][1] for i in range(n) for j in range(i, n)])
    found_ba = any([dp[i][1] and dp[j][0] for i in range(n) for j in range(i, n)])
    
    if found_ab or found_ba:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
