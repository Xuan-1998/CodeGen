def partition(s):
    if len(s) == 1:
        return s, ""
    mid = len(s) // 2
    left, right = s[:mid], s[mid:]
    return left, right

def is_scrambled(s1, s2):
    if len(s1) != len(s2):
        print(False)
    elif sorted(s1) != sorted(s2):
        print(False)
    else:
        def is_partition_scrambled(s1, s2):
            if len(s1) == 0:
                print(True)
                return
            left1, right1 = partition(s1)
            left2, right2 = partition(s2)
            if left1 + right1 != left2 + right2:
                print(False)
                return
            is_partition_scrambled(right1, right2)

        is_partition_scrambled(s1, s2)

import sys

s1 = input().strip()
s2 = input().strip()

is_scrambled(s1, s2)
