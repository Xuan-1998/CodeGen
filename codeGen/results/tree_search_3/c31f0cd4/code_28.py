def get_subset_sums(set):
    n = len(set)
    dp = [[set[0]] for _ in range(n + 1)]
    
    for i in range(1, n):
        for j in range(i, -1, -1):
            subset_sum = sum(dp[j])
            if subset_sum not in set:
                dp[i].append(subset_sum)
                
    return sorted(list(set(set) | set(map(sum, (x for x in dp)))))
