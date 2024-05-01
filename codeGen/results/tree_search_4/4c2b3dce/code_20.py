code = """
s = input()
found_ab = False
found_ba = False

for i in range(len(s)):
    if s[i:i+2] == "AB":
        found_ab = True
    elif s[i:i+2] == "BA":
        found_ba = True

if found_ab and found_ba:
    print("YES")
else:
    print("NO")
"""

print(code)
