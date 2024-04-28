def find_distinct_sums(set_size, num_elements):
    dp = {}
    for i in range(num_elements + 1):
        subset_sum = 0
        for j in range(i + 1):
            subset_sum += min(j, set_size)
        if subset_sum not in dp:
            dp[subset_sum] = []
        dp[subset_sum].append(subset_sum)

    return ' '.join(map(str, sorted(dp.keys())))

N = int(input())
A = list(map(int, input().split()))
print(find_distinct_sums(N, len(A)))
