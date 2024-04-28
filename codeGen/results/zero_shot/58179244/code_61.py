n = int(input())
s = input()

r, t = 0, ''
for i in range(n):
    if i == 0:
        if s[i] in ['G', 'B']:
            r += 1
            t += 'R'
        else:
            t += s[i]
    elif i == n-1:
        if s[i] in ['G', 'R']:
            r += 1
            t += 'B'
        else:
            t += s[i]
    else:
        if s[i] == s[i-1]:
            if s[i] == 'R':
                if s[i+1] != 'G':
                    r += 2
                    t = t[:i] + 'G' + t[i+1:] + 'B'
                elif s[i+1] != 'B':
                    r += 2
                    t = t[:i] + 'B' + t[i+1:] + 'G'
            else:
                if s[i+1] != 'R':
                    r += 2
                    t = t[:i] + 'R' + t[i+1:] + 'B'
                elif s[i+1] != 'B':
                    r += 2
                    t = t[:i] + 'G' + t[i+1:] + 'R'
            if s[i] == 'G':
                if s[i-1] == 'R':
                    r += 1
                    t = t[:i-1] + 'B' + t[i:]
                elif s[i-1] == 'B':
                    r += 1
                    t = t[:i-1] + 'R' + t[i:]

print(r)
print(t)
