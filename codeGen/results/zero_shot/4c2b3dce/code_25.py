import sys
s = sys.stdin.readline().strip()
if 'AB' in s and 'BA' in s[1:]:
    print('YES')
else:
    print('NO')
