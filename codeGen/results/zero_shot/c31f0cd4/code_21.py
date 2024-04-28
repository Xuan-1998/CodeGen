n = int(input())
a = list(map(int, input().split()))
s = set()
for i in range(1 << n):
    temp_sum = 0
    for j in range(n):
        if ((i >> j) & 1):
            temp_sum += a[j]
    s.add(temp_sum)
print(' '.join(map(str, sorted(list(s)))))
