def solve(s, a):
    n = len(s)
    ways = 0
    longest_substring_len = 0
    min_substrings = float('inf')

    for i in range(n):
        # Initialize variables to track the current substring
        curr_substring_len = 1
        curr_substring_ending_index = i

        while curr_substring_ending_index < n:
            # Check if the current substring satisfies the condition
            curr_substring_letter_count = sum(1 for c in s[curr_substring_ending_index - curr_substring_len + 1:curr_substring_ending_index + 1] if ord(c) - ord('a') < a[ord(c) - ord('a')] or (c == 'z' and curr_substring_letter_count == 1))

            if curr_substring_letter_count <= a[ord(s[curr_substring_ending_index]) - ord('a')]:
                # Update the results
                ways += 1
                longest_substring_len = max(longest_substring_len, curr_substring_len)
                min_substrings = min(min_substrings, curr_substring_len)

            curr_substring_len += 1

    return ways % (10**9 + 7), longest_substring_len, min_substrings
