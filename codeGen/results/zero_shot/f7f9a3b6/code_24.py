code start here
num_ways = 0
longest_substring_length = 0
min_num_substrs = float('inf')  # initialized with infinity

for char in s:
    for i in range(26):
        if ord(char) - ord('a') == i:  # check if the character is in the English alphabet
            num_consecutive_appearances = min(a[i], n - len(s[:n-1].replace(chr(ord('a')+i)), 1))
            num_ways *= (num_consecutive_appearances + 1)
            longest_substring_length = max(longest_substring_length, num_consecutive_appearance)
            min_num_substrs = min(min_num_substrs, n // num_consecutive_appearances)

print(num_ways % (10**9 + 7))
print(longest_substring_length)
print(min_num_substrs)
