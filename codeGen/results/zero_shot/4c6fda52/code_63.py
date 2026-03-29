# Step 1: Read the input
n, k = map(int, input().split())
s = input()

# Step 2: Calculate the number of 'R's at the beginning of s
r_count = s[:k].count('R')

# Step 3: Calculate the minimum number of characters that need to be changed in s
min_changes = r_count

# Step 4: Iterate through the string s and find the maximum number of 'R's in a substring of length k
max_r_count = 0
for i in range(n - k + 1):
    max_r_count = max(max_r_count, s[i:i+k].count('R'))

# Step 5: Calculate the minimum number of characters that need to be changed in s
min_changes = min(min_changes, k - max_r_count)

# Step 6: Print the result
print(min_changes)
