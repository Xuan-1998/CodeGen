import sys

def has_ab_and_ba(s):
    a_index = s.find('A')
    b_index = s.find('B')

    while True:
        if a_index + 1 < len(s) and s[a_index + 1] == 'B':
            if b_index >= a_index + 2 or (b_index != -1 and s[b_index: b_index + 3].find('AB') != -1):
                return "YES"
        if b_index + 1 < len(s) and s[b_index + 1] == 'A':
            if a_index >= b_index + 2 or (a_index != -1 and s[a_index: a_index + 3].find('BA') != -1):
                return "YES"

        a_index = s.find('A', a_index + 1)
        b_index = s.find('B', b_index + 1)

    return "NO"

s = sys.stdin.readline().strip()
print(has_ab_and_ba(s))
