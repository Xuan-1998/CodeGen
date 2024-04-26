def has_non_overlapping_AB_BA(s):
    # Find the first occurrence of "AB"
    ab_pos = s.find("AB")
    # If found, look for "BA" after "AB" + 2 positions to ensure non-overlapping
    if ab_pos != -1 and "BA" in s[ab_pos + 2:]:
        return True

    # Find the first occurrence of "BA"
    ba_pos = s.find("BA")
    # If found, look for "AB" after "BA" + 2 positions to ensure non-overlapping
    if ba_pos != -1 and "AB" in s[ba_pos + 2:]:
        return True

    return False

# Read input from stdin
s = input().strip()

# Check for non-overlapping "AB" and "BA"
if has_non_overlapping_AB_BA(s):
    print("YES")
else:
    print("NO")
