s = input()
max_len = 0
ans = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if s[i:j] == s[i:j][::-1]:
            if len(s[i:j]) > max_len:
                max_len = len(s[i:j])
                ans = s[i:j]
print(ans)
