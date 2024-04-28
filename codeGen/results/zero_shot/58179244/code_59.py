n = int(input())
s = input()
r = 0
t = list(s)

for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        if t[i] == 'R':
            t[i] = 'G'
            t[i+1] = 'B'
        elif t[i] == 'G':
            t[i] = 'B'
            t[i+1] = 'R'
        else:
            t[i] = 'R'
            t[i+1] = 'G'

print(r)
print(''.join(t))
