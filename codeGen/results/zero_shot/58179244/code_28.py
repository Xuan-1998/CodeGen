n = int(input())
s = input()
r, t = 0, s
prev_color = s[0]
for i in range(1, n):
    if s[i] == prev_color:
        r += 1
        if s[i] == 'R':
            t = t[:i] + 'G' + t[i+1:]
        elif s[i] == 'G':
            t = t[:i] + 'B' + t[i+1:]
        else:
            t = t[:i] + 'R' + t[i+1:]
    prev_color = s[i]
print(r)
print(t)
