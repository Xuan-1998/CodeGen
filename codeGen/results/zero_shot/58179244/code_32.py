n = int(input())
s = input()

r = 0
t = s
for i in range(n-1):
    if s[i] == s[i+1]:
        r += 1
        t = list(t)
        t[i] = 'R' if s[i] == 'G' else 'G' if s[i] == 'B' else 'B'
        t = ''.join(t)

print(r)
print(t)
