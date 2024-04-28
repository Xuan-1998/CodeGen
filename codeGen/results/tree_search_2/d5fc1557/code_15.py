def longest_subarray(nums):
    n = len(nums)
    f = [0] * (n + 1)  # store the results of subproblems

    for i in range(1, n + 1):
        if nums[i - 1] == 1:  # found a 1
            f[i] = max(f[i - 1], 1)  # update the longest subarray length
        else:  # found a 0, reset the longest subarray length
            f[i] = 0

    return max(f[1:])  # find the maximum value in the array (excluding the first element)

def delete_and_find_longest_subarray(nums):
    n = len(nums)
    if all(x == 0 for x in nums):  # edge case: only zeros
        return 0
    longest_length = longest_subarray(nums)
    return longest_length

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        nums = [int(x) for x in f.read().split()]
    print(delete_and_find_longest_subarray(nums))
