from collections import defaultdict

def subsetSums(nums):
    memo = {0: [[]]}
    total_sum = sum(nums)
    res = []

    for num in nums:
        new_memo = defaultdict(list)
        for (curr_sum, subsets) in list(memo.items()):
            for subset in subsets:
                new_subset = set(subset + [num])
                new_sum = curr_sum + num
                if len(new_subset) < len(nums):  # avoid duplicates
                    new_memo[new_sum].append(list(new_subset))
        memo = dict(new_memo)

    for (curr_sum, subsets) in list(memo.items()):
        for subset in subsets:
            if len(res) == 0 or curr_sum != res[-1]:
                res.append(curr_sum)
            break

    return sorted(res)


def main():
    N = int(input())
    nums = [int(x) for x in input().split()]
    print(*subsetSums(nums), sep=' ')


if __name__ == "__main__":
    main()
