n = int(input())
counts = [0] * (n + 1)
for i in range(10**n):
    s = format(i, '0{}d'.format(n))
    count = 1
    for j in range(1, len(s)):
        if s[j] == s[0]:
            count += 1
        else:
            counts[count] += 1
            count = 1
    counts[count] += 1

print(*counts, sep=' ')
