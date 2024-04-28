import sys

s = input().strip()

found_ab = False
found_ba = False

for i in range(len(s)):
    if s[i:i+2] == 'AB' and not found_ab:
        found_ab = True
    elif s[i:i+2] == 'BA' and found_ab:
        found_ba = True
        break

if found_ab and found_ba:
    print('YES')
else:
    print('NO')

