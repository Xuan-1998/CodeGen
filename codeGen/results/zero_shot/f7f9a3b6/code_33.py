def split_message(s):
    # Initialize variables to store the results
    num_ways = 0
    max_length = 0
    min_substrings = float('inf')

    # Iterate over all possible splits of the message
    for i in range(1, len(s)):
        # Check if the current split satisfies the condition
        current_substring = s[:i]
        for char in set(current_substring):
            count = sum(1 for c in current_substring if c == char)
            if count > a[ord(char) - ord('a')]:
                break
        else:
            # If the split satisfies the condition, update the results
            num_ways += 1
            max_length = max(max_length, i)
            min_substrings = min(min_substrings, len(s) // i)

    return num_ways % (10**9 + 7), max_length, min_substrings

n = int(input())
s = input()
a = [int(x) for x in input().split()]

num_ways, max_length, min_substrings = split_message(s)

print(num_ways)
print(max_length)
print(min_substrings)
