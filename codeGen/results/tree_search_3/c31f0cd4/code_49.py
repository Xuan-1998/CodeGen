def find_sum_combinations(nums):
    nums.sort()
    sums = [0]
    for num in nums:
        new_sums = []
        for total in sums:
            new_sums.append(total + num)
        sums += new_sums
    
    return sorted(set(sums))

# Example usage:
input_nums = list(map(int, input().split()))
print(" ".join(str(num) for num in find_sum_combinations(input_nums)))
