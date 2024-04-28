n = int(input())
s = input()
r = 0
t = s[:]

for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        t = list(t)
        j = i + (i % 2 == 0)
        k = (j + 1) % 3
        t[j] = chr(ord('RGB'[k]) + ord('A'))
        t = ''.join(t)

print(r)
print(t)
