from collections import Counter

def check_string(s):
    count_a = s.count('A')
    count_b = s.count('B')

    if (count_a == len(s) and 'B' in s) or (count_b == len(s) and 'A' in s):
        return "YES"
    else:
        return "NO"

s = input()
print(check_string(s))
