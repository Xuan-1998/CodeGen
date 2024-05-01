def find_abba(s):
    if len(s) < 2:
        return "NO"

    for i in range(len(s) - 1):
        if s[i:i+2] == "AB" and s[i+2:] != "":
            if s[i+2:].find("BA") != -1:
                return "YES"
        elif s[i:i+2] == "BA":
            if s[:i].find("AB") != -1:
                return "YES"

    return "NO"


# Receive input from stdin
s = input()

# Print the answer to stdout
print(find_abba(s))
