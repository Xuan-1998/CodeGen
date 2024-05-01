def has_ab_and_ba(s):
    ab_exists = False
    ba_exists = False

    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB':
            ab_exists = True
        elif s[i:i+2] == 'BA' and not ab_exists:
            ba_exists = True
        elif s[i:i+2] == 'AB' and ba_exists:
            return "YES"
    return "NO"

# Read input from standard input
s = input()

print(has_ab_and_ba(s))
