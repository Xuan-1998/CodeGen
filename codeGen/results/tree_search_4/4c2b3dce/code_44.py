code = input().strip()
ab = code.find('AB')
ba = code.find('BA')

if ab != -1 and (code[ab+2:].find('BA') != -1):
    print("YES")
else:
    print("NO")
