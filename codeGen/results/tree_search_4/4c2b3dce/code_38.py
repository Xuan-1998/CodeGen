===BEGIN CODE===
def find_ab_ba(s):
    found_ab = False
    found_ba = False
    
    for i in range(len(s)):
        if s[i:i+2] == "AB" and not found_ab:
            found_ab = True
            i += 1  # Update the pointer to avoid overlapping
        elif s[i:i+2] == "BA" and not found_ba:
            found_ba = True
            i += 1  # Update the pointer to avoid overlapping
        
        if found_ab and found_ba:
            return "YES"
    
    return "NO"

s = input()
print(find_ab_ba(s))
===END CODE===
