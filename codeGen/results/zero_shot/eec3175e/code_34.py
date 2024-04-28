n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(1 if any(sum(subset) % m == 0 for L in range(0, len(nums)+1), r=enumerate(reduce(lambda x,y: x+y,[[]]+[list(i) for i in itertools.combinations(nums, r)]))) else 0)
