def check_substrings(s):
    index_ab = s.find("AB")
    index_ba = s.find("BA")

    # Check if "AB" is found and look for "BA" after "AB"
    if index_ab != -1 and "BA" in s[index_ab + 2:]:
        return "YES"
    
    # Check if "BA" is found and look for "AB" after "BA"
    if index_ba != -1 and "AB" in s[index_ba + 2:]:
        return "YES"

    return "NO"

# Reading input from stdin
s = input().strip()
print(check_substrings(s))
