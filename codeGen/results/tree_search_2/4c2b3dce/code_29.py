import sys

def solve():
    s = input().strip()
    
    dp = [False] * (len(s) + 1)
    
    for i in range(2, len(s) + 1):
        if (s[i-2:i] == 'AB' and not dp[i-2]) or (s[i-2:i] == 'BA' and not dp[i-3]):
            dp[i] = True
        else:
            dp[i] = False
    
    print("YES" if dp[-1] else "NO")

if __name__ == "__main__":
    solve()
