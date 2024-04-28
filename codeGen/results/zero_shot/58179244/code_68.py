n = int(input())
s = input()
r, t = 0, ''
prev_color = s[0]
for i in range(1, n):
    if s[i] == prev_color:
        r += 1
        t += 'R' if s[i-1] == 'G' else ('G' if s[i-1] == 'B' else 'B')
    prev_color = s[i]
print(r)
print(t)
