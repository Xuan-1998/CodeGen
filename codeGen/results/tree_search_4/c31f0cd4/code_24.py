def subset_sums(set):
    dp = {0: set([0])}
    for num in set:
        new_dp = {}
        for k, sums in dp.items():
            for sum_val in sums:
                new_dp[k] = new_dp.get(k, set()) | {sum_val + num}
                if k > 0:
                    new_dp[k-1] = new_dp.get(k-1, set()) | {sum_val}
        dp = new_dp
    return set.union(*dp.values())

N = int(input())
set = set(map(int, input().split()))
print(' '.join(map(str, subset_sums(set))))
