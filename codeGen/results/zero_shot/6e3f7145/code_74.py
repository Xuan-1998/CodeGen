s = input()
max_length = 0
start_index = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substring = s[i:j]
        if substring == substring[::-1] and len(substring) > max_length:
            max_length = len(substring)
            start_index = i
print(s[start_index:start_index+max_length])
