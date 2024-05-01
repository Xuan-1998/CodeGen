def find_distinct_sums(sets):
    def generate_subsets(remain_set, subset_sum=0, memo={}):
        if subset_sum not in memo:
            memo[subset_sum] = []
        if remain_set == set():
            memo[subset_sum].append(subset_sum)
        else:
            for i in range(len(remain_set)):
                elem = remain_set.pop()
                new_subset_sum = subset_sum + elem
                generate_subsets(remain_set, new_subset_sum, memo)
                remain_set.add(elem)

    distinct_sums = []
    for s in sets:
        remaining_set = set(s)
        generate_subsets(remaining_set)
        for k in sorted(memo.keys()):
            if len(memo[k]) > 0:
                distinct_sums.append(k)

    return " ".join(str(x) for x in distinct_sums)


# read input
N = int(input())
sets = []
for _ in range(N):
    sets.append(set(map(int, input().split())))

print(find_distinct_sums(sets))
