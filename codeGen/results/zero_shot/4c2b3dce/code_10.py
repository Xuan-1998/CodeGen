def contains_AB_and_BA(s):
    # First, search for "AB" followed by "BA"
    index_AB = s.find("AB")
    if index_AB != -1:
        # Start searching for "BA" after "AB"
        if s.find("BA", index_AB + 2) != -1:
            return "YES"
    
    # Next, search for "BA" followed by "AB"
    index_BA = s.find("BA")
    if index_BA != -1:
        # Start searching for "AB" after "BA"
        if s.find("AB", index_BA + 2) != -1:
            return "YES"
    
    return "NO"

# Read input from stdin
s = input().strip()
print(contains_AB_and_BA(s))
