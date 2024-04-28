def find_sums(nums):
    n = len(nums)
    max_sum = sum(nums)
    sums = [0] * (max_sum + 1)

    for subset in range(2 ** n):
        current_sum = 0
        for bit in range(n):
            if (subset >> bit) & 1:
                current_sum += nums[bit]
        sums[current_sum] += 1

    return ' '.join(map(str, [sum for sum, count in enumerate(sums) if count]))

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(find_sums(nums))
