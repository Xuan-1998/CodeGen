python
# Step 1: Understand the Problem
The problem is to find the length of the longest increasing subsequence (LIS) in an unsorted array of integers.

# Step 2: Define a Dynamic Programming Approach
We can use dynamic programming to solve this problem. The key idea is to maintain a dp array where dp[i] represents the length of the LIS ending at index i.

# Step 3: Initialize the DP Array
dp = [1] * len(array)  # Initialize dp array with all ones

# Step 4: Fill up the DP Table
for i in range(1, len(array)):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# Step 5: Find the Maximum Length
max_length = max(dp)

print(max_length)  # Print the length of the longest increasing subsequence
