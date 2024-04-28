n = int(input())
s = input()

r = 0
t = s
for i in range(1, n):
    if t[i-1] == t[i]:
        r += 1
        t = list(t)
        t[i] = 'R' if t[i] != 'R' else 'G' if t[i] != 'G' else 'B'
        t = ''.join(t)

print(r)
print(t)
