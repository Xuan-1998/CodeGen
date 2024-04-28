n = int(input())
s = input()

count_R = 0
count_G = 0
count_B = 0

for i in range(n):
    if s[i] == 'R':
        count_R += 1
    elif s[i] == 'G':
        count_G += 1
    else:
        count_B += 1

if n % 2 != 0 and (count_R % 2 != 0 or count_G % 2 != 0):
    r = min(count_R, count_G)
elif n % 2 != 0 and count_B % 2 != 0:
    r = count_B
elif n % 2 == 0 and (count_R % 2 != 0 or count_G % 2 != 0 or count_B % 2 != 0):
    if max(count_R, count_G, count_B) >= min(count_R, count_G, count_B) + 1:
        r = min(count_R, count_G, count_B)
    else:
        r = max(count_R, count_G, count_B) - min(count_R, count_G, count_B) + 1
else:
    if (count_R + count_G) % 2 != 0 and count_B % 2 == 0:
        r = min(count_R, count_G)
    elif count_R % 2 == 0 and (count_G + count_B) % 2 != 0:
        r = min(count_G, count_B)
    else:
        if max(count_R, count_G, count_B) >= min(count_R, count_G, count_B) + 1:
            r = min(count_R, count_G, count_B)
        else:
            r = max(count_R, count_G, count_B) - min(count_R, count_G, count_B) + 1

t = s[:r]

print(r)
print(t)
