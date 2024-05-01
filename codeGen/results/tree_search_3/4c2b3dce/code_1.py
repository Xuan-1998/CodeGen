def has_abba(s):
    for i in range(len(s) - 2):
        if s[i:i+2] == 'AB' and s[i+2:] == 'BA':
            return True
    return False

print('YES' if has_abba(input()) else 'NO')
