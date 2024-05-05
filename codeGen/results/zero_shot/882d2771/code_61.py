import sys
t, l, r = map(int, input().split())

# Step 1: Think about the problem statement and identify the key elements
# The function f(n) represents the minimum number of comparisons needed to select the most beautiful participant from n girls.

# Step 2: Realize that we don't need to know the exact value of f(n), but only its values at certain indices (l, l+1, ..., r).
# This allows us to focus on calculating these specific values instead of trying to find a general formula for f(n).

# Step 3: Notice that f(l) + f(l+1) + ... + f(r) represents the total number of comparisons needed.
# We can calculate this by considering each girl as a "node" in a tree, and the girls' beauty scores as their "weights".
# The minimum number of comparisons for each group is equivalent to the longest increasing subsequence (LIS) problem.

# Step 4: Realize that we can use dynamic programming to solve the LIS problem.
# Initialize a table dp[i] representing the length of the longest increasing subsequence ending at node i.
# Then, iterate through all nodes and update dp[i] based on the maximum value of dp[j] where j is smaller than i.

def lis(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

# Step 5: Calculate the value of f(l), f(l+1), ..., f(r) and store them in an array.
f_values = [lis([i, l+i, r+i]) for i in range(t)]

# Step 6: Finally, calculate the desired expression t0·f(0) + t1·f(1) + ... + tr - l·f(r) modulo 109+7.

result = sum(i*f_values[i] for i in range(t)) - l*lis([l+r])

print(result % (10**9 + 7))
