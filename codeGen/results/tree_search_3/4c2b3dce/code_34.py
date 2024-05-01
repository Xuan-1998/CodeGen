import sys

def solve():
    s = input().strip()
    dp = [False] * (len(s) + 1)
    
    for i in range(2, len(s)):
        if s[i-1] == 'A' and s[i] == 'B':
            dp[i+1] = True
        elif s[i-1] == 'B' and s[i] == 'A':
            dp[i] = True
    
    if (dp[-3] or dp[1]) and (dp[-4] or dp[0]):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
