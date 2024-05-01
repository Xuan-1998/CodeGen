import sys

def solution():
    s = input().strip()

    for i in range(len(s) - 1):
        window = set(s[:i+2])
        if 'AB' in window or 'BA' in window:
            remaining = s[i+2:]
            if 'AB' in remaining or 'BA' in remaining:
                return "YES"

    return "NO"

print(solution())
