def find_pattern(s):
    memo = {}
    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB':
            if 'BA' in s[i+2:]:
                return "YES"
            elif i + len(s) - 3 >= len(s):  # i.e., there are at most two characters left
                return "NO"
    return "NO"

s = input()
print(find_pattern(s))
