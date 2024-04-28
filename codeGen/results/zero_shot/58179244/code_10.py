n = int(input())
s = input()
r = 0
t = list(s)

for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        t[i+1] = 'B' if t[i] != 'B' else 'G'

print(r)
print(''.join(t))
