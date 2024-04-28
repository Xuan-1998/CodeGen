i = 0
while i < len(s):
    if s[i] == 'B':
        j = i - 1
        while j >= 0 and s[j] != 'A':
            j -= 1
        if j >= 0:
            print("YES")
            break
    i += 1
else:
    print("NO")

