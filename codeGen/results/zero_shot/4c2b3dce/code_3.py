def check_AB_BA(s):
    index_AB = s.find("AB")
    index_BA = s.find("BA")

    # Check if both substrings are found and non-overlapping
    if index_AB != -1 and index_BA != -1:
        # Check for non-overlapping with a gap of at least one character
        if abs(index_AB - index_BA) > 1:
            return "YES"
        # If they are overlapping, try to find another occurrence of "BA" after "AB"
        elif index_AB < index_BA:
            return "YES" if "BA" in s[index_AB + 2:] else "NO"
        # If they are overlapping, try to find another occurrence of "AB" after "BA"
        else:
            return "YES" if "AB" in s[index_BA + 2:] else "NO"
    else:
        return "NO"

# Read input from stdin
s = input().strip()
print(check_AB_BA(s))
