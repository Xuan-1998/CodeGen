import sys

def solve():
    s = input()
    ab = 'AB'
    ba = 'BA'

    i, j = 0, len(ba) - 1
    found_ab, found_ba = False, False

    for c in s:
        if i < len(ab):
            if c == ab[i]:
                i += 1
            elif c == ab[0]:
                i = 0
                j = len(ba) - 1
                found_ab = True
        if j >= 0 and (c == ba[j] or c == ba[0]):
            if c == ba[j]:
                j -= 1
            else:
                i, j = 0, len(ba) - 1
                found_ba = True

    return 'YES' if found_ab and found_ba else 'NO'

print(solve())
