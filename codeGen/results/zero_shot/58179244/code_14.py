n = int(input())
s = input()
r = 0
t = list(s)
for i in range(1, n):
    if t[i] == t[i-1]:
        r += 1
        if t[i] == 'R':
            t[i] = 'G'
        elif t[i] == 'G':
            t[i] = 'B'
        else:
            t[i] = 'R'
print(r)
print(''.join(t))
