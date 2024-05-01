from collections import defaultdict

def get_distinct_sums(a):
    # Initialize hashmap to store subsets and their sums
    dp = defaultdict(set)
    dp[0].add(0)

    for num in a:
        temp_dp = defaultdict(set)
        for subset_sum, subset in dp.items():
            for x in range(subset_sum + 1, subset_sum + num + 1):
                temp_dp[x].add(x)
        dp.update(temp_dp)

    return ' '.join(map(str, sorted(list(dp.values())[0])))
