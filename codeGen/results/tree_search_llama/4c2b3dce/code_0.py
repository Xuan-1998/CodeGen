def find_substring(s, target, found):
    if len(s) < len(target):
        return False
    for i in range(len(s) - len(target) + 1):
        if s[i:i+len(target)] == target:
            if not found and (target == 'AB' or target == 'BA'):
                return True
            else:
                remaining = s[i+len(target):]
                return find_substring(remaining, target, True)
    return False

s = input()
if find_substring(s, 'AB', False) or find_substring(s, 'BA', False):
    print('YES')
else:
    print('NO')
