import sys

def solve():
    s = input()
    ab_found, ba_found = False, False
    dp = [[False] * (len(s) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s)):
        if s[i-1:i+1] == "AB":
            ab_found = True
        elif s[i-1:i+1] == "BA":
            ba_found = True

        dp[i][i] = ab_found and ba_found
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == "AB" or s[i:j] == "BA":
                if not (ab_found and ba_found):
                    dp[i][j-1] = True
                break

    print("YES" if ab_found and ba_found else "NO")

if __name__ == "__main__":
    solve()
