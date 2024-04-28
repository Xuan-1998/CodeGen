n = int(input())
s = input()

r = 0
t = s[:]

for i in range(1, n):
    if t[i-1] == t[i]:
        r += 1
        if t[i-1] == 'R':
            t = t[:i] + 'G' + t[i+1:]
        elif t[i-1] == 'G':
            t = t[:i] + 'B' + t[i+1:]
        else:
            t = t[:i] + 'R' + t[i+1:]

print(r)
print(t)
