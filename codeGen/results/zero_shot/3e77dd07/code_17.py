def is_scrambled(s1, s2):
    scrambled_strings = get_scrambled_strings(s1)
    for scrambled_string in scrambled_strings:
        if scrambled_string == s2:
            return True
    return False

# Example usage:
s1 = input()
s2 = input()
if is_scrambled(s1, s2):
    print("True")
else:
    print("False")
