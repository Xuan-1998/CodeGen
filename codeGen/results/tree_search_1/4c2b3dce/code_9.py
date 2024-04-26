def contains_non_overlapping_AB_BA(s):
    # Search for "AB" from the start
    pos_ab = s.find("AB")
    while pos_ab != -1:
        # Search for "BA" after "AB"
        pos_ba = s.find("BA", pos_ab + 2)
        if pos_ba != -1:
            return "YES"
        # Move to the next occurrence of "AB"
        pos_ab = s.find("AB", pos_ab + 1)
    
    # Search for "BA" from the start
    pos_ba = s.find("BA")
    while pos_ba != -1:
        # Search for "AB" after "BA"
        pos_ab = s.find("AB", pos_ba + 2)
        if pos_ab != -1:
            return "YES"
        # Move to the next occurrence of "BA"
        pos_ba = s.find("BA", pos_ba + 1)
    
    return "NO"

# Read input from stdin
s = input().strip()

# Output the result
print(contains_non_overlapping_AB_BA(s))
