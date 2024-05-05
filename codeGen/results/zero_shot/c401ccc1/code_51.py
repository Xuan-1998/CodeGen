while v != 0:
    if v & u != v:
        print("NO")
        break
    v = v & u

if v == 0:
    print("YES")
