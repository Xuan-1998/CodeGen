n = int(input())
s = input()
r, t = 0, ''
for i in range(n):
    if i > 0 and s[i] == s[i-1]:
        r += 1
    else:
        t += s[i]
print(r)
print(t)
