def check_AB_BA(s):
    first_AB = -1
    first_BA = -1

    # Search for "AB" then "BA"
    for i in range(len(s) - 1):
        if s[i:i+2] == "AB" and first_AB == -1:
            first_AB = i
        elif s[i:i+2] == "BA" and first_AB != -1 and i - first_AB > 1:
            return "YES"

    # Reset indices
    first_AB = -1
    first_BA = -1

    # Search for "BA" then "AB"
    for i in range(len(s) - 1):
        if s[i:i+2] == "BA" and first_BA == -1:
            first_BA = i
        elif s[i:i+2] == "AB" and first_BA != -1 and i - first_BA > 1:
            return "YES"

    return "NO"

# Read input from stdin
s = input().strip()

# Output the result
print(check_AB_BA(s))
