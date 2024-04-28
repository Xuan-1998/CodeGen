n = int(input())
s = input()

r = 0
t = s[:]
for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        t[i] = 'R' if t[i] == 'G' else 'G' if t[i] == 'B' else 'B'
print(r)
print(t)
