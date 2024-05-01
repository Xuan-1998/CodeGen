def generate_sums(a):
    total_set = set()
    for i in range(2**len(a)):
        temp_sum = 0
        for j in range(len(a)):
            if (i >> j) & 1:
                temp_sum += a[j]
        total_set.add(temp_sum)
    return sorted(list(total_set))

a = list(map(int, input().split()))
print(' '.join(map(str, generate_sums(a))))
