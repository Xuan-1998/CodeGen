n = int(input())
s = input()
r = 0
t = s[:]
for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        for j in range(i, n-1):
            if t[j] != t[j+1]:
                t = list(t)
                t[i:j+2] = ['R' if c == 'G' else 'G' if c == 'B' else 'B' for c in t[i:j+2]]
                t = ''.join(t)
                break
print(r, t)
