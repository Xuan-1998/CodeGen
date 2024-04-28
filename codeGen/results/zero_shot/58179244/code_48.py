n = int(input())
s = input()

r = 0
t = list(s)
for i in range(1, n):
    if t[i-1] == t[i]:
        r += 1
        t[i] = 'R' if t[i] == 'G' else 'G' if t[i] == 'B' else 'B'

print(r)
print(''.join(t))
