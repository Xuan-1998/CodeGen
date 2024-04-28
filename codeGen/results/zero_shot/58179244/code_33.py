n = int(input())
s = input()

r, t = 0, ''
for i in range(n):
    if (i == 0 or s[i] != s[i-1]) and (t[i] != 'R' or r % 3 != 2) and (t[i] != 'G' or r % 3 != 1) and (t[i] != 'B' or r % 3 != 0):
        t += s[i]
    else:
        t += ['R', 'G', 'B'][[(s[i-1] == 'R', 2), (s[i-1] == 'G', 1), (s[i-1] == 'B', 0)][0]]
        r += 1
print(r)
print(t)
