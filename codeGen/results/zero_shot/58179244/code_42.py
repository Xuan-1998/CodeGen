n = int(input())
s = input()
r = 0
t = ''
for i in range(n):
    if s[i-1] == s[i]:
        r += 1
        t += 'B' if s[i] != 'B' else 'G' if s[i] != 'G' else 'R'
    else:
        t += s[i]
print(r)
print(t)
