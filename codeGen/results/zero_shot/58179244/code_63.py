n = int(input())
s = input()

r = 0
t = list(s)

for i in range(n):
    if t[i] == 'R':
        t[i] = 'G'
    elif t[i] == 'G':
        t[i] = 'B'
    else:
        r += 1
print(r)
print(''.join(t))
