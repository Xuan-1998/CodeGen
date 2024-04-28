i = int(input())
s = input().upper()
count_A = count_B = 0

for c in s:
    if c == 'A':
        count_A += 1
    elif c == 'B':
        count_B += 1

if (count_A >= 1 and count_B >= 1) or (count_A >= 2 and count_B >= 0) or (count_A >= 0 and count_B >= 2):
    print("YES")
else:
    print("NO")

