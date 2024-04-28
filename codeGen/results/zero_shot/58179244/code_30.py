n = int(input())
s = input()

r = 0
t = list(s)
for i in range(n-1):
    if t[i] == t[i+1]:
        r += 1
        for j in range(i, n-1):
            if t[j] != t[j+1]:
                t[i] = t[j+1]
                break

print(r)
print(''.join(t))
