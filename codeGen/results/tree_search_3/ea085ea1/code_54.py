# Receive inputs from stdin
str1 = input().strip()
str2 = input().strip()

# Calculate the maximum number of common substrings
max_len = max_common_substrings(str1, str2)

# Print the answer to stdout
print(max_len)
