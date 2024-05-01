import sys

def findAB(s):
    n = len(s)
    dp = [False] * (n + 1)
    for i in range(n - 1, -1, -1):
        if s[i:i+2] == "BA" or s[i:i+2] == "AB":
            return 1
        elif s[i] == 'B':
            dp[i] = True
        else:
            if i > 0 and dp[i-1]:
                dp[i] = True
    return 0

def main():
    s = input().strip()
    print("YES" if findAB(s) else "NO")

if __name__ == "__main__":
    main()
