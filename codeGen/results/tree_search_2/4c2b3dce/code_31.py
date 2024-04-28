count_A = 0
count_B = 0

for char in input().strip():
    if char == 'A':
        count_A += 1
    elif char == 'B':
        count_B += 1

if abs(count_A - count_B) >= 2:
    print('YES')
else:
    print('NO')
