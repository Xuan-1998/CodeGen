def min_cuts(s):
    n = len(s)
    cuts = [0] * (n + 1)
    for i in range(2, n + 1):
        j = i - 1
        while j >= 0 and s[j] == s[i]:
            j -= 1
        if j < 0:
            cuts[i] = 0
        else:
            cuts[i] = cuts[j + 1] + 1
    return sum(cuts[2:] - cuts[1:-1])

s = input()
print(min_cuts(s))
