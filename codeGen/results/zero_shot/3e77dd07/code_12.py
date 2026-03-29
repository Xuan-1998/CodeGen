def areScrambled(s1, s2):
    if len(s1) != len(s2):
        return False

    def isScrambledUtil(s1, s2):
        if not s1 and not s2:
            return True
        if not s1 or not s2:
            return False
        
        count1 = 0
        count2 = 0
        for i in range(len(s1)):
            if s1[i] == '1':
                count1 += 1
            if s2[i] == '1':
                count2 += 1

        return isScrambledUtil(s1[:count1], s2[:count2]) and isScrambledUtil(s1[count1:], s2[count2:])

    return isScrambledUtil(s1, s2)

s1 = input()
s2 = input()

print(areScrambled(s1, s2))
