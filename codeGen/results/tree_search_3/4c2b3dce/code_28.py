code = """
i, j = 0, 0
while i < len(s):
    if s[i:i+2] == "AB":
        while j < len(s) and s[j:j+2] == "BA":
            print("YES")
            exit()
        j = i + 2
    i += 1
print("NO")
"""
