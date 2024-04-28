n = int(input())
s = input()
r, t = 0, s
for i in range(n):
    if (i > 0 and s[i] == s[i-1]) or i == 0:
        r += 1
        if s[i] == 'R':
            t = t[:i] + 'G' + t[i+1:]
        else:
            t = t[:i] + 'B' + t[i+1:]
print(r)
print(t)
