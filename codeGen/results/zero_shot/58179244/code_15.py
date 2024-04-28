n = int(input())
s = input()
r = 0
t = s
for i in range(n):
    if (i == 0 or t[i-1] == t[i]) and t[i] != 'B':
        r += 1
        t = list(t)
        if t[i] == 'R':
            t[i] = 'G'
        else:
            t[i] = 'R'
print(r)
print(''.join(t))
