import sys

def find_smallest_string():
    n, k = map(int, input().split())
    s = input()

    # Generate all possible strings of length k
    if k <= n:
        poss_strings = [s[:k]]
    else:
        poss_strings = [s + s[:k - n]]

    for i in range(n):
        new_s = s[:i] + s[i+1:]
        if len(new_s) + 1 <= k:
            poss_strings.append(new_s)
        elif len(new_s) * 2 <= k:
            poss_strings.append(new_s + new_s[:k - len(new_s)])

    # Find the lexicographically smallest string
    return min(poss_strings)

print(find_smallest_string())
