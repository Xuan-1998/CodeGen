import sys

def is_palindrome(s):
    return s == s[::-1]

def min_cuts(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n + 1):
            if is_palindrome(s[i:j]):
                dp[i][j] = True
            else:
                for k in range(i, j):
                    if dp[i][k] and dp[k + 1][j]:
                        dp[i][j] = True
                        break

    cuts = 0
    for i in range(1, n + 1):
        if not dp[0][i]:
            cuts += 1

    return cuts - 1  # subtract 1 because we count the last cut as well

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
