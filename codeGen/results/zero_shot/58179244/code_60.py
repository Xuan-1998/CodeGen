import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
r = 0
t = s
for i in range(1, n):
    if t[i-1] == t[i]:
        r += 1
        t = list(t)
        t[i] = {'R': 'G', 'G': 'B', 'B': 'R'}[t[i]]
        t = ''.join(t)
print(r)
print(t)
