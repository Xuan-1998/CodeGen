def get_distinct_sums(nums):
    memo = {}
    distinct_sums = set()

    def subset_sums(nums, start, current_sum):
        if current_sum not in memo:
            memo[current_sum] = 0
        memo[current_sum] += 1

        for i in range(start, len(nums)):
            new_sum = current_sum + nums[i]
            subset_sums(nums, i+1, new_sum)

    subset_sums(nums, 0, 0)
    distinct_sums = set(memo.keys())
    return sorted(list(distinct_sums))

def main():
    N = int(input())
    nums = [int(x) for x in input().split()]
    print(" ".join(map(str, get_distinct_sums(nums))))

if __name__ == "__main__":
    main()
