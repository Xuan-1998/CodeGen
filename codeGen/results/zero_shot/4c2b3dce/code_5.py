code
s = input()
found_ab = s.find("AB") != -1
if found_ab:
    remaining_string = s[found_ab + 2:]
    if remaining_string.find("BA") != -1:
        print("YES")
else:
    if s.find("BA") != -1:
        print("YES")
else:
    print("NO")
