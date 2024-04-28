n = int(input())
s = input()
r = 0
t = list(s)
for i in range(1, n):
    if t[i-1] == t[i]:
        r += 1
        t[i] = {'R': 'G', 'G': 'B', 'B': 'R'}[t[i-1]]
print(r)
print(''.join(t))
