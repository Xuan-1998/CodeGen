def find_distinct_sums(nums):
    n = len(nums)
    max_sum = sum(nums)
    distinct_sums = set()

    for i in range(1 << n):  # Generate all subsets
        subset_sum = 0
        for j in range(n):
            if (i & (1 << j)):  # Check if the jth number is included in the subset
                subset_sum += nums[j]
        
        if subset_sum <= max_sum:  # To avoid overflow
            distinct_sums.add(subset_sum)  # Store the sum in a set for uniqueness

    return ' '.join(map(str, sorted(list(distinct_sums))))


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    
    print(find_distinct_sums(nums))
