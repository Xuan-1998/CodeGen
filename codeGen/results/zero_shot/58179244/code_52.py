n = int(input())
s = input()
r, t = 0, s
for i in range(n):
    if (i == 0 or t[i-1] != 'R' and t[i] == 'R') or (i == n-1 or t[i+1] != 'G' and t[i] == 'G'):
        r += 1
        if i < n-1:
            if t[i+1] == 'B':
                t = t[:i+1] + 'G' + t[i+2:]
            elif t[i+1] == 'G':
                t = t[:i+1] + 'R' + t[i+2:]
        else:
            if t[i] == 'B':
                t = t[:i] + 'G'
            elif t[i] == 'G':
                t = t[:i] + 'R'
    elif (i == 0 or t[i-1] != 'G' and t[i] == 'G') or (i == n-1 or t[i+1] != 'B' and t[i] == 'B'):
        r += 1
        if i < n-1:
            if t[i+1] == 'R':
                t = t[:i+1] + 'G' + t[i+2:]
            elif t[i+1] == 'G':
                t = t[:i+1] + 'B' + t[i+2:]
        else:
            if t[i] == 'R':
                t = t[:i] + 'G'
            elif t[i] == 'B':
                t = t[:i] + 'R'
print(r)
print(t)
