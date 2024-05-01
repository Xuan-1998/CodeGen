while True:
    try:
        s = input()
        break
    except EOFError:
        pass

found_ab = False
found_ba = False

i, j = 0, len(s) - 1

while i < len(s) and not found_ab:
    if s[i:i+2] == "AB":
        found_ab = True
    i += 1

if not found_ab:
    print("NO")
else:
    while j >= 0 and not found_ba:
        if s[j:j+2] == "BA":
            found_ba = True
        j -= 1

    if found_ba:
        print("YES")
    else:
        print("NO")
