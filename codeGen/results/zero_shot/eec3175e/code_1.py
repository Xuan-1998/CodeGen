n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(int(any(sum(possible) % m == 0 for r in range(len(nums)+1) for possible in combinations(nums, r))))
