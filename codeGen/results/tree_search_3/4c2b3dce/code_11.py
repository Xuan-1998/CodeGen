def solve():
    s = input().strip()
    found_ab = False

    for i in range(len(s) - 1):
        if s[i:i+2] == "AB":
            found_ab = True
            if s[i+2:i+4] == "BA":
                print("YES")
                return
        elif s[i:i+2] == "BA" and not found_ab:
            print("NO")
            return

    if not found_ab:
        print("YES")

solve()
