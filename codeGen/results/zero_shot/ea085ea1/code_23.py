import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

preprocessed_str1 = ''.join(c for c in str1 if c in '*#@')
preprocessed_str2 = ''.join(c for c in str2 if c in '*#@')

def find_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return substrings

substrings_str1 = find_substrings(preprocessed_str1)
substrings_str2 = find_substrings(preprocessed_str2)

common_substrings = set()
for substring in substrings_str1:
    if substring in substrings_str2:
        is_common = True
        for common_substring in common_substrings:
            if common_substring.startswith(substring) or common_substring.endswith(substring):
                is_common = False
                break
        if is_common:
            common_substrings.add(substring)

print(len(common_substrings))
