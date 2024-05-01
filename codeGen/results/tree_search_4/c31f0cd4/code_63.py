from collections import defaultdict

def find_subset_sums(nums):
    dp = defaultdict(set)
    dp[set(), 0] = {0}

    for num in nums:
        for i in range(len(dp)):
            curr_sum = sum(list(dp[i]))
            if curr_sum + num not in dp[i]:
                dp[i].add(curr_sum + num)
                find_subset_sums(list(dp[i]))

    return sorted({sum(1 for subset in dp[()] if subset)})

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    print(" ".join(map(str, find_subset_sums(nums))))
