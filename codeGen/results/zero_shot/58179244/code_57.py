n = int(input())
s = input()
r, t = 0, ''
prev_color = s[0]
for i in range(1, n):
    if s[i] == prev_color:
        r += 1
        t += 'R' if prev_color == 'G' else 'G' if prev_color == 'B' else 'B'
    else:
        t += s[i]
    prev_color = s[i]
print(r)
print(t)
