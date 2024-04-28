import itertools
n = int(input())
nums = list(map(int, input().split()))
solutions = set()
for r in range(1, n + 1):
    for subset in itertools_chain(itertools.combinations(nums, r)):
        solutions.add(sum(subset))

print(' '.join(map(str, sorted(solutions))))
