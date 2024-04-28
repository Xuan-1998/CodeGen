n = int(input())
s = input()

r = 0
t = list(s)

for i in range(n):
    if (i > 0 and t[i] == t[i-1]):
        r += 1
        if t[i] == 'R':
            t[i] = 'G'
        else:
            t[i] = 'B'

print(r)
print(''.join(t))
