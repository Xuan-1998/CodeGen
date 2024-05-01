code = input()
ab_count = code.count('AB')
ba_count = code.count('BA')

if ab_count > 0 and ba_count > 0:
    print("YES")
else:
    print("NO")
