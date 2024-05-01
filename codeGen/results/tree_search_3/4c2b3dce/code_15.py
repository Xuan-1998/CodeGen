while True:
    try:
        s = input()
        f = True
        i = 0
        while i < len(s):
            if f and s[i:i+2] == "AB":
                f = False
            elif not f and s[i:i+2] == "BA":
                f = False
            i += 1
        if f:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
