from collections import defaultdict

def solve():
    N = int(input())
    numbers = list(map(int, input().split()))
    dp = [[0] * (sum(numbers) + 1) for _ in range(N + 1)]
    
    # Helper function to generate all possible subsets of the given set
    def get_subsets(nums):
        subsets = []
        for i in range(2**len(nums)):
            subset = [num for j, num in enumerate(nums) if (i & (1 << j))]
            subsets.append(subset)
        return subsets
    
    # Generate all possible subsets and calculate their sums
    for i, num in enumerate(numbers):
        subsets = get_subsets(numbers[:i] + numbers[i+1:])
        for subset in subsets:
            dp[i][sum(subset)] += 1
    
    # Print out the distinct sums that can be generated from the subsets of the given set
    distinct_sums = set()
    for i in range(sum(numbers) + 1):
        if dp[N][i] > 0:
            distinct_sums.add(i)
    print(' '.join(map(str, sorted(list(distinct_sums)))))

if __name__ == "__main__":
    solve()
