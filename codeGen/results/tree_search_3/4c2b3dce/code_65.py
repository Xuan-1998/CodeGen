def check_abba(s):
    for i in range(len(s) - 2):  # We need at least two characters left after 'AB' or 'BA'
        if s[i:i+2] == "AB" and s[i+2:] == s[:i][::-1]:  # Check if we have 'AB' followed by its reverse
            return "YES"
    for i in range(len(s) - 2):
        if s[i:i+2] == "BA" and s[i+2:] == s[:i][::-1]:
            return "YES"
    return "NO"

s = input()
print(check_abba(s))
