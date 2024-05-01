from collections import defaultdict

def check_string():
    s = input()
    states = defaultdict(bool)
    seen_ab = False
    seen_ba = False

    for i, c in enumerate(s):
        if c == 'A':
            if i % 2 == 0 and s[i+1] == 'B' and not seen_ab:
                seen_ab = True
            else:
                states[(s[:i].count('A'), s[:i].count('B'))] = True
        elif c == 'B':
            if i % 2 != 0 and s[i-1] == 'A' and not seen_ba:
                seen_ba = True
            else:
                states[(s[:i].count('A'), s[:i].count('B'))] = True

    return "YES" if seen_ab and seen_ba else "NO"

print(check_string())
