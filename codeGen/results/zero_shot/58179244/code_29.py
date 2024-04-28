n = int(input())
s = input()
r = 0
t = list(s)
for i in range(1, n):
    if t[i-1] == t[i]:
        t[i] = 'B' if t[i] == 'R' else 'R'
        r += 1

print(r)
print(''.join(t))
