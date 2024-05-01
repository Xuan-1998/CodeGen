from itertools import chain, combinations

def powerset(s):
    return chain(*map(lambda x: combinations(s, x), range(0, len(s) + 1)))

def get_sums(s):
    s = set(map(int, s.split()))
    sums = {}
    for r in powerset(list(s)):
        sum_val = sum(r)
        if sum_val not in sums:
            sums[sum_val] = True
    return sorted(list(sums.keys()))

n = int(input())
s = input().split()
print(' '.join(map(str, get_sums(s))))
