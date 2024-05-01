def solve():
    n = int(input())
    s = input().upper()
    
    dp = [[False] * 2 for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        if s[i - 1] == 'A' and s[i - 2:i] == 'BA':
            dp[i][1] = True
        elif s[i - 1] == 'B' and s[i - 2:i] == 'AB':
            dp[i][0] = True
        
        for j in range(2):
            if not dp[i][j]:
                continue
            
            if j == 0:
                for k in range(i + 1, n + 1):
                    if s[k - 1] == 'B' and s[k - i - 1:k] == 'AB':
                        dp[k][1] = True
                        break
            else:
                for k in range(i + 1, n + 1):
                    if s[k - 1] == 'A' and s[k - i - 1:k] == 'BA':
                        dp[k][0] = True
                        break
    
    if dp[n][0] or dp[n][1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
