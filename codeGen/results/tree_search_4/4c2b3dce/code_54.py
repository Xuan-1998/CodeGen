import sys

def solve():
    s = input()
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s)):
        if i >= 2 and s[i-2:i] == "AB" or (s[i-1] == 'B' and s[i] == 'A'):
            dp[i] = dp[i-2]
        else:
            dp[i] = False
    print("YES" if dp[-2] else "NO")

if __name__ == "__main__":
    solve()
