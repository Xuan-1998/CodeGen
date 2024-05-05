def count_ways(s, a):
    num_ways = 1
    current_substring_length = 0
    for char in s:
        if a[ord(char) - ord('a')] > 0:
            current_substring_length += 1
            if current_substring_length > a[ord(char) - ord('a')]:
                return 0
        else:
            num_ways = (num_ways * (current_substring_length + 1)) % (10**9 + 7)
            current_substring_length = 0
    return num_ways

num_ways = count_ways(s, a)

longest_substring = max(a)  # the longest substring is the maximum of a
min_substrings = len(s) // max(a)  # the minimum number of substrings is the length of s divided by the maximum of a

print(num_ways)
print(longest_substring)
print(min_substrings)
