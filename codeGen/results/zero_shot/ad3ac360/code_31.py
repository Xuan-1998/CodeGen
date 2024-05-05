import sys

def palindrome_partition(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i, n+1):
            if s[i-1:j].is_palindrome():
                dp[i][j] = 0
            else:
                min_cuts = float('inf')
                for k in range(j-1, i-1, -1):
                    if dp[k][i].sum() + (dp[k+1][j].sum() or 0) < min_cuts:
                        min_cuts = dp[k][i].sum() + (dp[k+1][j].sum() or 0)
                dp[i][j] = [min_cuts]

    return sum(dp[-1])

def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    s = input()
    print(palindrome_partition(s))
