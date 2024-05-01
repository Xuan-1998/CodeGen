def max_common_substrings(str1, str2):
    memo = {}  # Memoization table

    def has_common_substring(i, j, length):
        # Check if there's a common substring of length 'length' at positions i and j
        for k in range(length):
            if str1[i+k] != str2[j+k]:
                return False
        return True

    max_length = 0
    max_count = 0

    for length in range(1, min(len(str1), len(str2))+1):
        for i in range(len(str1)-length+1):
            for j in range(len(str2)-length+1):
                if has_common_substring(i, j, length):
                    # If we've found a common substring of this length
                    # store the result in our memoization table
                    memo[(i, j, length)] = True

    for length in range(1, min(len(str1), len(str2))+1):
        count = 0
        for i in range(len(str1)-length+1):
            for j in range(len(str2)-length+1):
                if (i, j, length) in memo and (i+1, j+1, length) not in memo:
                    # If we've found a common substring of this length that doesn't overlap
                    # with any previously found substrings, increment our count
                    count += 1
        max_count = max(max_count, count)

    return max_count

str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
