n = int(input())
s = input()
r, t = 0, ''
i, j = 0, n-1
while i < j:
    if s[i] == s[j]:
        r += 1
        if s[i] == 'R':
            t += 'G'
            t += 'B' 
        elif s[i] == 'G':
            t += 'R'
            t += 'B' 
        else:
            t += 'R'
            t += 'G' 
    i, j = i+1, j-1
print(r)
print(t)
