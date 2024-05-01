code = input().strip()
last_two_chars = [None, None]
found_ab = found_ba = False

for char in code:
    if char == 'A':
        last_two_chars[0] = 'A'
        last_two_chars[1] = 'B' if not found_ab else None
        found_ab = found_ba or (last_two_chars[0] != 'A' and last_two_chars[1] != 'B')
    elif char == 'B':
        last_two_chars[0] = 'A' if not found_ab else None
        last_two_chars[1] = 'B'
        found_ba = found_ab or (last_two_chars[0] != 'B' and last_two_chars[1] != 'A')

if found_ab and found_ba:
    print('YES')
else:
    print('NO')
