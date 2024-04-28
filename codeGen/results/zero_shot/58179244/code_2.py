n = int(input())
s = input()

r = 0
t = s
for i in range(n):
    if (i == 0 or t[i-1] != t[i]) and (i == n-1 or t[i] != t[i+1]):
        continue
    else:
        r += 1
        t = list(t)
        for j in range(i, i+3):
            if j >= n:
                break
            if t[j] == 'R':
                t[j] = 'G'
            elif t[j] == 'G':
                t[j] = 'B'
            else:
                t[j] = 'R'
        t = ''.join(t)
print(r)
print(t)
