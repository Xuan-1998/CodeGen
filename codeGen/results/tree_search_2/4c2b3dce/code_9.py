import sys

def find_AB(s):
    n = len(s)
    dp = [False] * (n + 1)

    for i in range(n):
        if s[i:i+2] == 'AB':
            for j in range(i+2, n):
                if s[j:j+2] == 'BA':
                    dp[i+4] = True
                    break

    return "YES" if any(dp) else "NO"

s = input().strip()
print(find_AB(s))
