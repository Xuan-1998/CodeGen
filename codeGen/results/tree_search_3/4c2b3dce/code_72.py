===BEGIN CODE===
while True:
    try:
        s = input()
        if len(s) < 2:
            print("NO")
        else:
            ab_idx = s.find('AB')
            ba_idx = s.find('BA')
            if ab_idx != -1 and (ba_idx == -1 or s[ab_idx+2:ab_idx+len('BA')+2].find('BA') != -1):
                print("YES")
            else:
                print("NO")
    except:
        break
===END CODE===
