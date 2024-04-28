n = int(input())
s = input()
r, t = 0, ''
for i in range(n):
    if s[i] == 'R':
        r += 1
        t += 'G' if i % 2 else 'B'
    elif s[i] == 'G':
        r += 1
        t += 'R' if i % 2 else 'B'
    else:
        r += 1
        t += 'R' if i % 2 else 'G'
print(r)
print(t)
