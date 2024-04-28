n = int(input())
s = input()

r, t = 0, s
for i in range(n):
    if (i > 0 and t[i-1] == t[i]):
        r += 1
        t = list(t)
        if t[i] == 'R':
            t[i] = 'G'
        elif t[i] == 'G':
            t[i] = 'B'
        else:
            t[i] = 'R'
        t = ''.join(t)

print(r)
print(t)
