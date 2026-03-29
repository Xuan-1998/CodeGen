def max_bitwise_or(s):
    max_or = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            or_value = int(s[i:j], 2)
            if or_value > max_or:
                max_or = or_value

    return bin(max_or)[2:]

n = int(input())
s = input()
print(max_bitwise_or(s))
