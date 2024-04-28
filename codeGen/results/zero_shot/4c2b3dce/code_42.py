s = input()
print("YES" if "AB" in s and "BA" not in s[:s.index("AB")] or "BA" in s and "AB" not in s[:s.index("BA")] else "NO")
