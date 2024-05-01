import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# Preprocess the strings by sorting their characters
str1_sorted = ''.join(sorted(str1))
str2_sorted = ''.join(sorted(str2))

def find_common_substrings(str1_sorted, str2_sorted):
    max_length = 0
    count = 0

    i = j = 0
    while i < len(str1_sorted) and j < len(str2_sorted):
        if str1_sorted[i] == str2_sorted[j]:
            k = i
            while i < len(str1_sorted) and j < len(str2_sorted) and str1_sorted[i] == str2_sorted[j]:
                i += 1
                j += 1
            count += 1
            max_length = max(max_length, i - k)
        elif str1_sorted[i] < str2_sorted[j]:
            i += 1
        else:
            j += 1

    return count

max_count = find_common_substrings(str1_sorted, str2_sorted)
print(max_count)
