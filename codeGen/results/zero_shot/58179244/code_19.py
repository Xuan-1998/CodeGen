n = int(input())
s = input()

r = 0
t = s

for i in range(1, n):
    if s[i-1] == s[i]:
        r += 1
        t = t[:i] + ('R' if s[i-1] == 'G' else 'G' if s[i-1] == 'B' else 'B') + t[i:]

print(r)
print(t)
