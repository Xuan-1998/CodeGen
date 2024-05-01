from collections import defaultdict

def find_substrings(s):
    memo = defaultdict(bool)
    for i in range(len(s)):
        if s[i] == 'A':
            A_prev, B_prev, found_A, found_B = True, False, True, False
        else:
            A_prev, B_prev, found_A, found_B = False, True, False, True

        if (i > 0 and s[i-1] != 'B') or i == 0:
            for j in range(i+2, len(s)+1):
                if j > i + 2:
                    A_next, B_next = s[j-2], s[j-1]
                    if A_prev == (A_next == 'A' and found_A) and B_prev == (B_next == 'B' and found_B):
                        return "YES"
        memo[(A_prev, B_prev), (found_A, found_B)] = True
    return "NO"

s = input()
print(find_substrings(s))
