import sys

def solve(s):
    seen = set()
    if 'AB' in s:
        seen.add('AB')
        rest = s.replace('AB', '', 1)
        if 'BA' in rest and not any(t in rest for t in seen) and not any(s.startswith(t) for t in seen):
            return 'YES'
    if 'BA' in s:
        seen.add('BA')
        rest = s.replace('BA', '', 1)
        if 'AB' in rest and not any(t in rest for t in seen) and not any(s.startswith(t) for t in seen):
            return 'YES'
    return 'NO'

s = sys.stdin.readline().strip()
print(solve(s))
