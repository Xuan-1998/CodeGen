def is_scrambled(s1, s2):
    if len(s1) != len(s2):
        return False

    def is_scrambled_recursive(i1, i2, memo):
        if (i1, i2) in memo:
            return memo[(i1, i2)]

        if i1 == len(s1) and i2 == len(s2):
            return True

        if s1[i1] != s2[i2]:
            return False

        result = any(is_scrambled_recursive(i1 + 1, j, memo) for j in range(i2 + 1))
        result |= any(is_scrambled_recursive(i1, k, memo) or is_scrambled_recursive(j, i2, memo)
                       for j in range(i2) for k in range(i1))

        memo[(i1, i2)] = result
        return result

    return is_scrambled_recursive(0, 0, {})

s1 = input()
s2 = input()

print(is_scrambled(s1, s2))
