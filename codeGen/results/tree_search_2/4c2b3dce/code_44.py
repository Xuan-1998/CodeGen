s = input()

count_A, count_B = 0, 0

for c in s:
    if c == 'A':
        count_A += 1
    elif c == 'B':
        count_B += 1

if (count_A > count_B) or (count_B > count_A):
    print("NO")
else:
    print("YES")
