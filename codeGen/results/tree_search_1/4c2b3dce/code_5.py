def find_two_substrings(s):
    # Find 'AB' and then 'BA'
    ab_index = s.find('AB')
    if ab_index != -1:
        # Start searching for 'BA' after the 'AB' we found
        if s.find('BA', ab_index + 2) != -1:
            return "YES"
    
    # Find 'BA' and then 'AB'
    ba_index = s.find('BA')
    if ba_index != -1:
        # Start searching for 'AB' after the 'BA' we found
        if s.find('AB', ba_index + 2) != -1:
            return "YES"
    
    # If we didn't return "YES" yet, it means we didn't find what we're looking for
    return "NO"

# Read input from stdin
s = input().strip()

# Output the result to stdout
print(find_two_substrings(s))
