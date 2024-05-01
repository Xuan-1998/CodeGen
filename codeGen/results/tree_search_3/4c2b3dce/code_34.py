import sys

s = input().strip()

def contains_abba(s):
    if 'AB' not in s or 'BA' not in s:
        return 'NO'

    if 'AB' * (len(s) // 2) == s[: len(s) // 2]:
        return 'NO'

    return 'YES'

print(contains_abba(s))
