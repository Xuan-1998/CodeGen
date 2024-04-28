s1 = input().strip()
s2 = input().strip()

n = 0
for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        substr = s1[i:j]
        if substr in s2:
            n += 1

print(n)
