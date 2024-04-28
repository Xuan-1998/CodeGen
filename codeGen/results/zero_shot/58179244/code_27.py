n = int(input())
s = input()

r = 0
t = list(s)

for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        t[i] = 'R' if t[i] != 'R' else 'G' if t[i] != 'G' else 'B'
        
print(r)
print(''.join(t))
