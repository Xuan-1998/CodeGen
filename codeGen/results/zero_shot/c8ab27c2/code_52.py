s = input()
t = input()
min_len = float('inf')
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if all(c in t or c == '?' for c in sub): 
            continue
        min_len = min(min_len, len(sub))
print(min_len if min_len != float('inf') else -1)
