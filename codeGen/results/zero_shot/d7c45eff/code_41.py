n = int(input())
k = int(input())
s = input().strip()

possibilities = []
if k >= n:
    possibilities.append(s[:-1])  # Delete the last character
else:
    possibilities.append(s)  # Duplicate the original string
possibilities.append(s + s[:k-n])  # Duplicate and truncate if necessary

result = min(possibilities)
print(result)
