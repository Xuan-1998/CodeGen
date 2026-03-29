def isScramble(s1, s2):
    if len(s1) != len(s2):
        return False

    def helper(s1, s2):
        if sorted(s1) != sorted(s2):
            return False
        if len(s1) == 1:
            return True
        for i in range(len(s1)):
            if helper(s1[:i+1], s2[:i+1]) and helper(s1[i+1:], s2[i+1:]):
                return True
        return False

    return helper(s1, s2)

s1 = input()
s2 = input()

print(isScramble(s1, s2))
