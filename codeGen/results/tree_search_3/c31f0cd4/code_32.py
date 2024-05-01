from collections import defaultdict

def find_distinct_sums(arr):
    memo = defaultdict(set)
    max_sum = sum(arr)

    def dp(subset_sum, subset_index):
        if subset_sum > max_sum or not arr:
            return set()
        if (subset_sum, subset_index) in memo:
            return memo[(subset_sum, subset_index)]
        
        result = set()
        for i, x in enumerate(arr):
            new_subset_sum = subset_sum + x
            result.update(dp(new_subset_sum, i+1))
        result.add(subset_sum)
        memo[(subset_sum, subset_index)] = result
        return result

    return sorted(reduce(lambda a, b: a.union(b), [dp(0, 0), dp(sum(arr[:i+1]), i) for i in range(len(arr))])))


# Example usage:
N = int(input())
arr = list(map(int, input().split()))
print(' '.join(map(str, find_distinct_sums(arr))))
