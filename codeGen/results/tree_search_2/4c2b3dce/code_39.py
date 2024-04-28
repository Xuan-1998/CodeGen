s = input()
counts = {'A': 0, 'B': 0}
for c in s:
    if c == 'A':
        counts['A'] += 1
    elif c == 'B':
        counts['B'] += 1

if counts['A'] > 0 and counts['B'] > 0:
    print("YES")
else:
    print("NO")
