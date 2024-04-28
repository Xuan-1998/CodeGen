def longest_subarray(nums):
    max_ones = 0
    curr_ones = 0
    
    for num in nums:
        if num == 1:
            curr_ones += 1
            max_ones = max(max_ones, curr_ones)
        else:
            curr_ones = 0
    
    return max_ones - 1

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    
    print(longest_subarray(nums))

if __name__ == "__main__":
    main()
