import sys

def find_substrings(s):
    before_B = False
    has_AB_or_BA = False
    overlapping = False

    for c in s:
        if c == 'A':
            before_B = True
            has_AB_or_BA = False
            overlapping = False
        elif c == 'B':
            if before_B:
                has_AB_or_BA = True
            else:
                overlapping = True

    if has_AB_or_BA and not overlapping:
        print("YES")
    else:
        print("NO")

s = input()
find_substrings(s)
