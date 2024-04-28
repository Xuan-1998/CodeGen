import sys

def count_ways(m, N, arr):
    # Create a memoization table to store computed values
    memo = dict()

    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        
        if k == 0:  # Base case: sum equals N
            return 1
        elif i == m or k < 0:  # Base case: no more elements left or negative sum
            return 0
        
        total = dp(i + 1, k)  # Recurse without including the current element
        if k >= arr[i]:  # Include the current element in the sum
            total += dp(i + 1, k - arr[i])
        
        memo[(i, k)] = total  # Store computed value for future use
        return total

    return dp(0, N) % (10**9 + 7)

# Read input from stdin
m, N = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(count_ways(m, N, arr))
