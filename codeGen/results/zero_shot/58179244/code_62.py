n = int(input())
s = input()
r = 0
t = ''
for i in range(n):
    if s[i] == 'R':
        t += 'G' if i > 0 and s[i-1] == 'G' else 'B'
    elif s[i] == 'G':
        t += 'R' if i > 0 and s[i-1] == 'R' else 'B'
    else:
        t += 'G' if i > 0 and s[i-1] == 'G' else 'R'
    r = max(r, (t[i] != s[i]))
print(r)
print(t)
