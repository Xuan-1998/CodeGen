n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(any(sum(subset) % m == 0 for r in range(len(nums)+1) for subset in itertools.chain(*[combinations(nums, i) for i in range(0, len(nums)+1)])))
