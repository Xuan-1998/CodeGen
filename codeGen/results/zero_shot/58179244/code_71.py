n = int(input())
s = input()

r, t = 0, ''
for i in range(n):
    if s[i] == 'R':
        t += 'G' if r % 3 == 1 else 'B'
    elif s[i] == 'G':
        t += 'R' if r % 3 == 2 else 'B'
    else:
        t += 'R' if r % 3 == 0 else 'G'
    r += 1

print(r)
print(t)
