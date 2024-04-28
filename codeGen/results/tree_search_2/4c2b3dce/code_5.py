i = 0
found_AB = False
while i < len(s):
    seen_A = s[i] == 'A'
    seen_B = not seen_A and (i+1 < len(s) and s[i+1] == 'B')
    
    if seen_A and seen_B:
        found_AB = True
        break

    i += 1

if found_AB:
    remaining_str = s[i:]
    if 'BA' in remaining_str:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

