def contains_ab_and_ba(s):
    if len(s) < 2:
        return "NO"

    # Check for 'AB' followed by 'BA'
    if s[:2] == 'AB' and s[2:4] == 'BA':
        return "YES"
    
    # Check for 'BA' followed by 'AB'
    if s[:2] == 'BA' and s[2:4] == 'AB':
        return "YES"

    # If not found, recursively check the remaining part of the string
    if len(s) > 3:
        return contains_ab_and_ba(s[2:])

    return "NO"


# Receive input from stdin
s = input()

# Print the result to stdout
print(contains_ab_and_ba(s))
