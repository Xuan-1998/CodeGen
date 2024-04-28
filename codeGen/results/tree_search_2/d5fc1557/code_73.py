def longest_subarray(nums):
    n = len(nums)
    max_length = 0
    current_length = 0

    for i in range(n):
        if nums[i] == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0

    return max(max_length, current_length)

def delete_one(nums):
    n = len(nums)
    longest_subarray_size = longest_subarray(nums)
    nums.remove(min([i for i in range(n) if nums[i] == 1], key=lambda x: x))
    return longest_subarray(nums)

if __name__ == "__main__":
    import sys
    input_array = [int(x) for x in sys.stdin.readline().strip().split()]
    print(delete_one(input_array))
