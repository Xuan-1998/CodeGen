def check_string(s):
    i = 0
    while i < len(s) - 1:
        if s[i:i+2] == "AB":
            j = i + 2
            while j < len(s) - 1:
                if s[j:j+2] == "BA":
                    print("YES")
                    return
                j += 1
        i += 1
    print("NO")

s = input()
check_string(s)
