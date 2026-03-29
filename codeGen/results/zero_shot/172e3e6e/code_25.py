def prev_divisor(j):
    i = j // 2
    while i > 0 and j % i != 0:
        i //= 2
    return i

n, a = map(int, input().split())
pref_sum = [0]
for i in range(1, n):
    if a[i] % i == 0:
        pref_sum.append(pref_sum[-1] + (a[i] // i))
    else:
        pref_sum.append(pref_sum[-1])

total_good_subsequences = 0
for j in range(n-1, -1, -1):
    total_good_subsequences += pref_sum[j+1] - pref_sum[prev_divisor(j)]
print(total_good_subsequences % (10**9 + 7))
