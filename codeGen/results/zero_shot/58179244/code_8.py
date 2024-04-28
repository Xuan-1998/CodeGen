n = int(input())
s = input()

r = 0
t = list(s)

for i in range(1, n):
    if t[i] == t[i-1]:
        r += 1
        t[i] = {'R': 'G', 'G': 'B', 'B': 'R'}.get(t[i])

print(r)
print(''.join(t))
