def has_non_overlapping_ab_ba(s):
    ab_found = False
    ba_found = False
    i = 0
    while i < len(s)-1:
        if not ab_found and s[i:i+2] == 'AB':
            ab_found = True
            i += 2  # Skip to avoid overlap
        elif not ba_found and s[i:i+2] == 'BA':
            ba_found = True
            i += 2  # Skip to avoid overlap
        else:
            i += 1

        if ab_found and ba_found:
            return "YES"
    return "NO"

# Read input from stdin
s = input().strip()
print(has_non_overlapping_ab_ba(s))
