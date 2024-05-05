def is_scrambled(s1, s2):
    if len(s1) != len(s2):
        return False

    def helper(s1, s2):
        if not s1 and not s2:
            return True
        if not s1 or not s2:
            return False
        for i in range(len(s1)):
            temp_s1 = s1[:i] + s1[i+1:]
            temp_s2 = s2[:i] + s2[i+1:]
            if helper(temp_s1, temp_s2):
                return True
        return False

    return helper(s1, s2)

s1 = input()
s2 = input()

print(is_scrambled(s1, s2))
