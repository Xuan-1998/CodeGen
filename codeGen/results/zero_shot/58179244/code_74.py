n = int(input())
s = input()
r = 0
t = s
for i in range(n):
    if (i > 0 and t[i] == t[i-1]):
        r += 1
        t = list(t)
        t[i] = 'G' if t[i] in ['R', 'B'] else 'R'
        t = ''.join(t)
print(r)
print(t)
