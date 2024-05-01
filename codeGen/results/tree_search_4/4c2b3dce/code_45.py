import sys

def find_substrings(s):
    n = len(s)
    dp_ab = [False] * (n+1)
    dp_ba = [False] * (n+1)

    for i in range(2, n+1):
        if s[i-2:i] == "AB":
            dp_ab[i] = True

    for j in range(2, n+1):
        if s[j-2:j] == "BA":
            dp_ba[j] = True

    for i in range(n-1, 0, -1):
        if dp_ab[i]:
            for j in range(i-2, -1, -1):
                if dp_ba[j]:
                    return "YES"
    return "NO"

s = input().strip()
print(find_substrings(s))
