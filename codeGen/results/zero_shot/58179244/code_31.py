import sys
n = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())
r = 0
t = s[:]
for i in range(n - 1):
    if t[i] == t[i+1]:
        r += 1
        for j in range(i, n-1):
            if t[j] != t[j+1]:
                t[i:j+2] = list(set(t[i:j+2]))
                break
print(r)
print(''.join(t))
