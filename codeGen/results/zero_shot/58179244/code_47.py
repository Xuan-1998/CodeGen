n = int(input())
s = input()

r = 0
t = s
for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        t = list(t)
        t[i+1] = 'R' if t[i+1] == 'G' else 'G' if t[i+1] == 'B' else 'B'
        t = ''.join(t)

print(r)
print(t)
