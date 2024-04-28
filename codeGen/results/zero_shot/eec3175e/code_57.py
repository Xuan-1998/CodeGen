n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(1 if sum(i % m for i in nums) == 0 else 0)
