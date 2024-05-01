===BEGIN CODE===
from collections import defaultdict

def distinct_sum_sums(sets):
    sums = set()
    for subset in sets:
        total = 0
        for num in subset:
            total += num
        if total not in sums:
            sums.add(total)
    return sorted(list(sums))

N = int(input())
numbers = [int(x) for x in input().split()]
print(*distinct_sum_sums([set(numbers)]), sep=' ')
===END CODE===
