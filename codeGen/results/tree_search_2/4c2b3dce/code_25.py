import sys

def find_substrings():
    s = input().strip()
    dp = [[False] * (len(s) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s)):
        if s[i-1:i+2] == 'ABA':
            dp[i][i+2] = True

    for i in range(len(s)):
        for j in range(i+3, len(s)+1):
            if (dp[i][j-3] and s[i:i+2] == 'AB') or (dp[j-2][j] and s[j-2:j] == 'BA'):
                print("YES")
                return
    print("NO")

find_substrings()
