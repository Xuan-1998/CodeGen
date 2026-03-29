n = int(input())
s = input()
a = [int(x) for x in input().split()]

ways = 0
longest_substring_length = 0
min_substrings = float('inf')

current_length = 0
char_freqs = [0] * 26

for char in s:
    if char_freqs[ord(char) - ord('a')] <= a[ord(char) - ord('a')]:
        current_length += 1
        char_freqs[ord(char) - ord('a')] += 1
    else:
        # check if the current substring is valid
        if current_length > longest_substring_length:
            longest_substring_length = current_length

        # update the ways to split the string
        ways += 1
        min_substrings = min(min_substrings, current_length)

        current_length = 0
        char_freqs = [0] * 26

# handle the last substring
if current_length > longest_substring_length:
    longest_substring_length = current_length

ways += 1
min_substrings = min(min_substrings, current_length)

print(ways % (10**9 + 7))
print(longest_substring_length)
print(min_substrings)
