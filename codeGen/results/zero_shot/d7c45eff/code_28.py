n = int(input())
s = input()

if k == len(s):
    result = s
else:
    if s[-1] < chr(ord('a') + k - len(s)):
        # Delete the last character
        result = s[:-1]
    else:
        # Duplicate the string
        result = s * 2[:k]

print(result)
