code
from collections import defaultdict

def max_common_substrings(str1, str2):
    # Initialize hash sets for both strings
    set1 = set(str1)
    set2 = set(str2)

    # Initialize maximum number of common substrings found so far
    max_common = 0

    # Iterate over all possible substrings using a sliding window approach
    for length in range(1, min(len(str1), len(str2)) + 1):
        for i in range(len(str1) - length + 1):
            substring = str1[i:i+length]
            if substring in set2:
                max_common += 1

    return max_common
endcode
