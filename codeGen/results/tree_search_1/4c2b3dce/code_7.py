def contains_non_overlapping_ab_ba(s):
    ab_index = -1  # Initialize with an invalid index
    ba_index = -1  # Initialize with an invalid index

    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB':
            # Check if we have found a 'BA' before that does not overlap
            if ba_index != -1 and ba_index < i - 1:
                return 'YES'
            # Update the last index of 'AB'
            ab_index = i
        elif s[i:i+2] == 'BA':
            # Check if we have found an 'AB' before that does not overlap
            if ab_index != -1 and ab_index < i - 1:
                return 'YES'
            # Update the last index of 'BA'
            ba_index = i

    return 'NO'

# Read input from stdin
s = input().strip()

# Output the result to stdout
print(contains_non_overlapping_ab_ba(s))
