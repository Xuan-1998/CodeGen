s = input()
max_len = 0
result = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substring = s[i:j]
        if substring == substring[::-1]:
            if len(substring) > max_len:
                max_len = len(substring)
                result = substring
print(result)
