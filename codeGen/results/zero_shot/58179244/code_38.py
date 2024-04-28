n = int(input())
s = input()

r, t = 0, ''
for i in range(n):
    if s[i] == 'R':
        t += 'G'
        r += 1
    elif s[i] == 'G':
        t += 'B'
        r += 1
    else:
        t += 'R'
print(r)
print(t)
