n = int(input())
s = input()
r = 0
t = ''
for i in range(n-1):
    if s[i] == s[i+1]:
        r += 1
        t += s[i]
    else:
        t += s[i]
if s[-1] != s[0]:
    t += s[0]
else:
    t += 'R' if s[0] in ['G', 'B'] else 'G' if s[0] == 'R' else 'B'
print(r)
print(t)
