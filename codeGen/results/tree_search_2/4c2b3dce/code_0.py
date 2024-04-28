def contains_AB_BA(s):
    # Check if 'AB' appears as a suffix of the string
    if s.endswith('AB'):
        # If 'AB' is found, check if 'BA' appears in the remaining part
        remaining = s[:-2]
        if remaining.endswith('BA'):
            return "YES"
    # If 'AB' is not found, or even if it is but 'BA' is not found, return "NO"
    return "NO"

s = input()
print(contains_AB_BA(s))
