# Step 1: Read the input
n = int(input())
s = input()
a = list(map(int, input().split()))

# Step 2: Initialize variables for counting ways to split, longest substring length, and minimum number of substrings
ways_to_split = 0
longest_substring_length = 0
min_substrings = n

# Step 3: Iterate over the string to find the maximum consecutive appearance of each character
consecutive_appearances = [0] * 26
for char in s:
    index = ord(char) - ord('a')
    consecutive_appearances[index] += 1

# Step 4: Iterate over the array a to count ways to split and calculate longest substring length and minimum number of substrings
for i in range(26):
    max_consecutive_times = a[i]
    remaining_chars = n - max_consecutive_times * (i + 1)
    if remaining_chars >= 0:
        ways_to_split += min(remaining_chars, consecutive_appearances[i])
        longest_substring_length = max(longest_substring_length, max_consecutive_times * (i + 1))
        min_substrings = min(min_substrings, max_consecutive_times * (i + 1) + (n - remaining_chars) // (max_consecutive_times * (i + 1)) + 1)

# Step 5: Print the output
print(ways_to_split % (10**9 + 7))
print(longest_substring_length)
print(min_substrings)
