s = input()
max_len = 0
ans = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        substr = s[i:j+1]
        if substr == substr[::-1]:
            if len(substr) > max_len:
                max_len = len(substr)
                ans = substr
print(ans)
