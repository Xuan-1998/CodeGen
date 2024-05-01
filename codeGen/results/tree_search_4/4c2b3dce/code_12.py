import sys

def solve():
    s = input()
    dp = [[False] * (len(s) + 1) for _ in range(len(s) + 1)]
    
    for i in range(1, len(s) + 1):
        for j in range(i, len(s) + 1):
            if (s[j-1] == 'A' and s[i-1] == 'B') or (s[j-1] == 'B' and s[i-1] == 'A'):
                dp[i][j] = True
            elif i > 1:
                dp[i][j] = dp[i-1][j-1]
    
    if dp[-1][-1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
