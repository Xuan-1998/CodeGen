s = input()
max_length = 0
start = 0
for i in range(len(s)):
    for j in reversed(range(i+1)):
        if s[j:i+1] == s[i:j:-1]:
            if len(s[j:i+1]) > max_length:
                max_length = len(s[j:i+1])
                start = j
print(s[start:start+max_length])
