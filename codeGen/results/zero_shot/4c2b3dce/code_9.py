s = input()

if 'AB' in s:
    s = s.replace('AB', '', 1)  # remove the first occurrence of "AB"
    if 'BA' in s:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
