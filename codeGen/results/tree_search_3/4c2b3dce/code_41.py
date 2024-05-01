import sys

def solve():
    n = int(input())
    s = input()
    dp = [True] * (n + 1)
    
    for i in range(2, n):
        if s[i - 2:i] == 'AB' or s[i - 1:i + 1] == 'BA':
            dp[i] = False
        else:
            dp[i] = dp[i - 1]
    
    print("YES" if dp[n - 1] else "NO")

if __name__ == "__main__":
    solve()
