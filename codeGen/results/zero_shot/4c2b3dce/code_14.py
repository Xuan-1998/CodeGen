s = input()
if ("AB" in s) and (s[s.index("AB")+2:].find("BA") != -1):
    print("YES")
else:
    print("NO")
