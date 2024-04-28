n = int(input())
s = input()
r = 0
t = s

for i in range(n-1):
    if s[i] == s[i+1]:
        r += 1
        t = t[:i] + 'R' if s[i] == 'G' else ('B' if s[i] == 'R' else 'G') + t[i+1:]

print(r)
print(t)
