import itertools

def find_sums(nums):
    # Calculate the powerset of the input set
    power_set = [[]]
    for num in nums:
        power_set.extend([curr + [num] for curr in power_set])

    # Calculate the sums for each subset
    sums = {0}
    for subset in power_set[1:]:
        total = sum(subset)
        if total not in sums:
            sums.add(total)

    return sorted(list(sums))

# Read input from stdin and print output to stdout
N = int(input())
nums = list(map(int, input().split()))
print(' '.join(map(str, find_sums(nums))))
