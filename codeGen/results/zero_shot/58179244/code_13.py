n = int(input())
s = input()
r = 0
t = s
for i in range(1, n):
    if t[i-1] == t[i]:
        r += 1
        t = t[:i] + ('R' if t[i] == 'G' else 'G') + t[i+1:]
print(r)
print(t)
