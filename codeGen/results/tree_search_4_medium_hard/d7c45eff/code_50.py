import sys

def min_string(i):
    if i == 0:
        return ""
    elif i == 1:
        return s[:i]
    else:
        prev = min_string(i-1)
        if i > 1 and prev[i-2] <= s[i-1]:
            return prev[:-1]
        else:
            return prev + prev[-1]

n, k = map(int, input().split())
s = input()

print(min_string(k))
