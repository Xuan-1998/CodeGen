===BEGIN CODE===
from sys import stdin

seen = set()
found_ab = False
found_ba = False

for char in stdin.readline().strip():
    if char == 'A':
        seen.add('A')
    elif char == 'B':
        seen.add('B')

    if len(seen) == 2 and ('AB' in ''.join(sorted(list(seen))) or 'BA' in ''.join(sorted(list(seen)))):
        found_ab = True
        found_ba = True

if found_ab and found_ba:
    print("YES")
else:
    print("NO")
===END CODE===
