s = input()
max_len = 0
start_idx = 0
for i in range(len(s)):
    for j in reversed(range(i+1, len(s)+1)):
        if s[i:j] == s[i:j][::-1]:
            if j - i > max_len:
                max_len = j - i
                start_idx = i
print(s[start_idx:start_idx+max_len])
