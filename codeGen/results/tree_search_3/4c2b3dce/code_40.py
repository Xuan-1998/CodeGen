code
while len(s) >= 2:
    if s[:2] == 'AB':
        s = s[2:]
        if 'BA' in s:
            print("YES")
            break
    elif s[:2] == 'BA':
        s = s[2:]
        if 'AB' in s:
            print("YES")
            break
print("NO")
