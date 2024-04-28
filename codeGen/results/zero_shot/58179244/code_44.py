n = int(input())
s = input()

r = 0
t = s

for i in range(n-1):
    if s[i] == s[i+1]:
        r += 1
        t = list(t)
        t[i] = 'B' if t[i] != 'B' else ('R' if t[i] == 'G' else 'G')
        t = ''.join(t)

print(r)
print(t)
