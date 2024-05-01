===BEGIN PLAN===
State: View the problem as generating all subsets of the given set and compute their sums.
For each possible sum, we can determine if it is distinct by checking its presence in a set or array.
State: dp[i][j] represents whether a sum equal to 'j' can be generated using only numbers from 1 to 'i'. Initialize all elements of the 2D array with False.
Iterate over the given set. For each element 'k', update the corresponding elements in the 2D array based on whether or not 'k' is included in the subset.
Transition relationship: dp[i][j] = (dp[i-1][j-k] || dp[i-1][j]) if j >= k; else False
State: For each distinct sum found, add it to a set or array.
Output: Print the set of distinct sums.

==END PLAN==

===CODE STARTS HERE===
from collections import defaultdict

def find_distinct_sums(nums):
    n = len(nums)
    dp = [[False] * (sum(nums) + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i+1):
            if nums[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    sums = set()
    for i in range(1, n+1):
        for j in range(sum(nums) + 1):
            if dp[i][j]:
                sums.add(j)

    return ' '.join(map(str, sorted(list(sums))))


nums = list(map(int, input().split()))
print(find_distinct_sums(nums))
