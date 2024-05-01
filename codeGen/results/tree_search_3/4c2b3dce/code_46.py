===BEGIN CODE===
s = input()
countA, countB = 0, 0
foundAB, foundBA = False, False

for i in range(len(s)):
    if s[i] == 'A':
        countA += 1
    elif s[i] == 'B':
        countB += 1

    if countA >= 1 and countB >= 1:
        if not foundAB or not foundBA:
            print("YES")
            exit()
        else:
            break

if not foundAB and not foundBA:
    for i in range(len(s)):
        if s[i] == 'A':
            countA += 1
        elif s[i] == 'B':
            countB += 1

        if countA >= 2 and countB >= 1:
            print("YES")
            exit()
        elif countA >= 1 and countB >= 2:
            print("YES")
            exit()

    print("NO")

===END CODE===
