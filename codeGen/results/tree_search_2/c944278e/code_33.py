from functools import lru_cache

@lru_cache(None)
def is_winning_permutation(s):
    if len(s) == 1:
        return int(s) > 0

    score = 0
    for i in range(len(s)):
        if s[i] == '1':
            score += 2 ** (n - i - 1)

    return score > 0

@lru_cache(None)
def find_winning_permutations(s):
    if len(s) == 1:
        return [s]

    winning_permutations = []
    for i in range(len(s)):
        if s[i] == '1':
            remaining_teams = s[:i] + s[i+1:]
            for p in find_winning_permutations(remaining_teams):
                winning_permutations.append('0' + p)

    return [p for p in winning_permutations if is_winning_permutation(p)]

def solve():
    n = int(input())
    s = input()

    winning_permutations = find_winning_permutations(s)
    print('\n'.join(sorted(winning_permutations)))

solve()
