n = int(input())
nums = list(map(int, input().split()))
one_count = nums.count(1)
print(len(max(map(''.join, (filter(str.isdigit, g) for g in itertools.groupby(nums)) if all(x==1 for x in g), default=[]))))
