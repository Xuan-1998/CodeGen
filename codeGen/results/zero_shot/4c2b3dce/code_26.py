import sys

s = sys.stdin.readline().strip()

if 'AB' in s:
    remaining_part = s.replace('AB', '', 1)
    if 'BA' in remaining_part:
        print("YES")
else:
    print("NO")
