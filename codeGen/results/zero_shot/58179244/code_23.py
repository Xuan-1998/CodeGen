n = int(input())
s = input()
r = 0
t = s
for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        for j in range(i, -1, -1):
            if t[j] != t[i]:
                t = t[:j] + {'R': 'G', 'G': 'B', 'B': 'R'}[t[i]] + t[j+1:]
                break
print(r)
print(t)
