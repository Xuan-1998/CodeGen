n = int(input())
s = input()
r = 0
t = s
for i in range(n):
    if i > 0 and (s[i] == t[i-1]):
        r += 1
        if s[i] == 'R':
            t = t[:i] + 'G' + t[i+1:]
        elif s[i] == 'G':
            t = t[:i] + 'B' + t[i+1:]
        else:
            t = t[:i] + 'R' + t[i+1:]
print(r)
print(t)
