def find_substring(start, target):
    if start >= len(s) - 2:
        return False
    
    if s[start:start+2] == target:
        return True
    
    return find_substring(start + 1, target)

s = input()
if find_substring(0, 'AB') and find_substring(len(s)-2, 'BA'):
    print('YES')
else:
    print('NO')
