python
def check_subsequences(s):
    n = len(s)
    if n < 4:
        return "NO"
    
    found_AB = False
    found_BA = False
    index_AB = -1
    index_BA = -1
    
    # Iterate through the string to find the first occurrences of "AB" and "BA"
    for i in range(n - 1):
        if s[i:i+2] == "AB" and not found_AB:
            found_AB = True
            index_AB = i
        elif s[i:i+2] == "BA" and not found_BA:
            found_BA = True
            index_BA = i
        
        # If both are found, check for non-overlapping condition
        if found_AB and found_BA:
            if abs(index_AB - index_BA) > 1:
                return "YES"
    
    # Reset and check the reverse order
    found_AB = False
    found_BA = False
    index_AB = -1
    index_BA = -1
    
    for i in range(n - 1):
        if s[i:i+2] == "BA" and not found_BA:
            found_BA = True
            index_BA = i
        elif s[i:i+2] == "AB" and not found_AB:
            found_AB = True
            index_AB = i
        
        # If both are found, check for non-overlapping condition
        if found_AB and found_BA:
            if abs(index_AB - index_BA) > 1:
                return "YES"
    
    return "NO"

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().strip()
    print(check_subsequences(input))

