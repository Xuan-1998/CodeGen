# Define a memoization dictionary to store the subset sums
memo = {}

def get_subset_sums(nums):
    # Base case: empty set has sum 0
    if not nums:
        return [0]
    
    # Recursive function to generate all subset sums
    def rec(i, curr_sum):
        if i == len(nums):
            return [curr_sum]
        
        new_sums = []
        
        # If the current number is positive, consider both including and excluding it
        if nums[i] > 0:
            for prev_sum in rec(i + 1, curr_sum):
                new_sums.append(prev_sum)
            for prev_sum in rec(i + 1, curr_sum + nums[i]):
                new_sums.append(prev_sum + nums[i])
        
        # If the current number is negative or 0, only consider including it
        else:
            for prev_sum in rec(i + 1, curr_sum):
                new_sums.append(prev_sum)
            new_sums.append(curr_sum + nums[i])
        
        return new_sums
    
    return rec(0, 0)

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    
    subset_sums = get_subset_sums(nums)
    unique_sums = sorted(set(subset_sums))
    
    print(' '.join(str(sum) for sum in unique_sums))

if __name__ == "__main__":
    main()
