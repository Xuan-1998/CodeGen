import sys

s = sys.stdin.readline().strip()
count_a = s.count('A')
count_b = s.count('B')

if count_a > count_b:
    if 'BA' in s[count_a:]:
        print('YES')
    else:
        print('NO')
elif count_b > count_a:
    if 'AB' in s[:count_b]:
        print('YES')
    else:
        print('NO')
else:
    if 'AB' in s and 'BA' in s:
        print('YES')
    else:
        print('NO')

