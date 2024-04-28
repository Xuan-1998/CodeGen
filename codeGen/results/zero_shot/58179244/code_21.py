n = int(input())
s = input()

r = 0
t = list(s)

for i in range(n):
    if t[i] == t[(i+1)%n]:
        r += 1
        t[i] = 'G' if t[i] == 'R' else 'R'

print(r)
print(''.join(t))
